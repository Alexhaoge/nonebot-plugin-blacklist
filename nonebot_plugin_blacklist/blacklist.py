from typing import Literal
from sqlalchemy import select, delete

from .utils import use_ac_session, use_redis_client
from .orm import BlacklistORM, SettingORM

async def check_blacklist(id: int | str, type_: Literal['userlist', 'grouplist', 'privlist']) -> bool:
    async with use_redis_client() as client:
        if type_ == 'privlist':
            monit_private = await client.get('blacklist_private')
            if not monit_private:
                return False
        on_blacklist = await client.sismember(f'blacklist_{type_}', str(id))
        if on_blacklist:
            return True
        else:
            return False
        
async def add_blacklist(ids: list[str], type_: Literal['userlist', 'grouplist', 'privlist']):
    async with use_redis_client() as client:
        await client.sadd(f'blacklist_{type_}', *ids)
    
    if type_ == 'userlist':
        type_int = 1
    elif type_ == 'grouplist':
        type_int = 2
    else:
        type_int = 3
    
    async with use_ac_session() as session:
        for id in ids:
            exists_bl = (await session.execute(select(BlacklistORM).filter_by(id=id, type_=type_int))).first()
            if not exists_bl:
                session.add(BlacklistORM(id=id, type_=type_int))
        await session.commit()

async def del_blacklist(ids: list[str], type_: Literal['userlist', 'grouplist', 'privlist']):
    async with use_redis_client() as client:
        await client.srem(f'blacklist_{type_}', *ids)
    
    if type_ == 'userlist':
        type_int = 1
    elif type_ == 'grouplist':
        type_int = 2
    else:
        type_int = 3
    
    async with use_ac_session() as session:
        for id in ids:
            exists_bl = (await session.execute(select(BlacklistORM).filter_by(id=id, type_=type_int))).first()
            if exists_bl:
                await session.delete(exists_bl[0])
        await session.commit()

async def clearall_blacklist():
    async with use_redis_client() as client:
        await client.delete('userlist', 'grouplist', 'privlist')
    async with use_ac_session() as session:
        await session.execute(delete(BlacklistORM))
        await session.commit()

async def view_blacklist(type_: Literal['userlist', 'grouplist', 'privlist']):
    async with use_redis_client() as client:
        return await client.smembers(f'blacklist_{type_}')


async def get_setting(type_: Literal['private', 'ban_auto_sleep']):
    async with use_redis_client() as client:
        setting = await client.get(f'blacklist_{type_}')
        return setting if setting else False
    
async def set_setting(type_: Literal['private', 'ban_auto_sleep'], value: bool):
    async with use_redis_client() as client:
        await client.set(f'blacklist_{type_}', int(value))
    async with use_ac_session() as session:
        exists_setting = (await session.execute(select(SettingORM).filter_by(key=type_))).first()
        if exists_setting:
            exists_setting[0].value = value
        else:
            session.add(SettingORM(type_, value))
        await session.commit()


async def load_db_to_redis():
    types = ['userlist', 'grouplist', 'privlist']
    async with use_ac_session() as session:
        async with use_redis_client() as client:
            stmt = select(SettingORM)
            async for x in await session.stream_scalars(stmt):
                await client.set(f'blacklist_{x.key}', int(x.value))
            stmt2 = select(BlacklistORM)
            async for x in await session.stream_scalars(stmt2):
                await client.sadd(f'blacklist_{types[x.type_ - 1]}', x.id)

__all__ = [
    'check_blacklist', 'add_blacklist', 'del_blacklist', 'view_blacklist', 'clearall_blacklist',
    'get_setting', 'set_setting',
    'load_db_to_redis'
]