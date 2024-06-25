from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User():
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]