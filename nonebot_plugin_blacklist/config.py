from typing import Literal, Optional

from nonebot import get_driver
from pydantic.v1 import BaseSettings

class Config(BaseSettings):
    redis_url: str = 'redis://localhost'
    class Config:
        extra = "ignore"

_conf: Optional[Config] = None


def conf() -> Config:
    global _conf
    if _conf is None:
        _conf = Config(**get_driver().config.dict())
    return _conf
