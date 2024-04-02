from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column


class BlacklistORM(MappedAsDataclass, Model):
    __tablename__ = "bl_blacklist"
    __table_args__ = {"extend_existing": True}

    id: Mapped[str] = mapped_column(primary_key=True)
    type_: Mapped[int] = mapped_column(primary_key=True)


class SettingORM(MappedAsDataclass, Model):
    __tablename__ = "bl_setting"
    __table_args__ = {"extend_existing": True}

    key: Mapped[str] = mapped_column(primary_key=True)
    value: Mapped[bool] = mapped_column(nullable=False)