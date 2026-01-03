from datetime import datetime

from sqlalchemy import BIGINT, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, TableNameMixin, int_pk


class User(Base, TableNameMixin, TimestampMixin):
    id: Mapped[int_pk] = mapped_column(BIGINT)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    full_name: Mapped[str | None]
    username: Mapped[str | None]
    language: Mapped[str] = mapped_column(String, server_default="en")

    referrer_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    #  joinedload - для m2o и o2o связей
    #  selectinload - для o2m и m2m связей
