"""Init DB

Revision ID: ac8a7b6e1275
Revises: 
Create Date: 2024-04-01 11:11:37.240334

"""
from typing import Sequence, Union
from pathlib import Path
from alembic import op
import sqlalchemy as sa
import json

# revision identifiers, used by Alembic.
revision: str = 'ac8a7b6e1275'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = ("nonebot_plugin_blacklist", )
depends_on: str | Sequence[str] | None = None

setting_keys = ['ban_auto_sleep', 'private']
type_keys = ['userlist', 'grouplist', 'privlist']

def upgrade(name: str = "") -> None:
    if name:
        return
    bind = op.get_bind()
    blacklist_table = op.create_table(
        "bl_blacklist",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("type_", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", "type_")
    )
    setting_table = op.create_table(
        'bl_setting',
        sa.Column("key", sa.String(), primary_key=True),
        sa.Column("value", sa.Boolean(), nullable=False)
    )

    json_path = Path("data/blacklist/blacklist.json")
    if json_path.exists():
        blacklist_json = json.load(json_path.open("r", encoding="utf-8"))
        
        for k in setting_keys:
            if k in blacklist_json:
                op.execute(setting_table.insert().values(key=k, value=blacklist_json[k]))
        
        for i, type_ in enumerate(type_keys):
            if type_ in blacklist_json:
                for id in blacklist_json[type_]:
                    op.execute(blacklist_table.insert().values(id=str(id), type_=i+1))
    bind.commit()

def downgrade(name: str = "") -> None:
    if name:
        return
    blacklist = dict()
    bind = op.get_bind()
    cursor = bind.execute("SELECT key, value FROM bl_setting;")
    for k, v in cursor.fetchall():
        blacklist[k] = v
    cursor2 = bind.execute("SELECT id, type_ FROM bl_blacklist;")
    for id, type_int in cursor.fetchall():
        type_ = type_keys[type_int+1]
        if not type_ in blacklist:
            blacklist[type_] = []
        blacklist[type_].append(str(id))
    
    data_path = Path("data/blacklist")
    data_path.mkdir(parents=True, exist_ok=True)
    with open(data_path/"blacklist.json", 'w', encoding='utf-8') as f:
        json.dump(blacklist, f)

    op.drop_table("bl_blacklist")
    op.drop_table("bl_setting")
