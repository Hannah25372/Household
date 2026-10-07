from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database.enums import Role, Bill
from datetime import date

from .database import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    role: Mapped[Role] = mapped_column()

class Split(Base):
    __tablename__ = "split"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Bill] = mapped_column()
    ratio: Mapped[float] = mapped_column()
    users: Mapped[str] = mapped_column()
    start_date: Mapped[date] = mapped_column()
    end_date: Mapped[date | None] = mapped_column()
    one_off: Mapped[bool] = mapped_column(default=False)


class Expense(Base):
    __tablename__ = "expense"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Bill] = mapped_column()
    amount: Mapped[float] = mapped_column()
    start_date: Mapped[date] = mapped_column()
    end_date: Mapped[date | None] = mapped_column()
    one_off: Mapped[bool] = mapped_column(default=False)

    # Constraints:
    # - Can only have one of each Bill with end_date None and one_off False
    # - Cannot have overlapping dates in the same Bill with one_off False
    # - Cannot have one_off True and end_date not None
    # - Cannot have one_off True and multiple BIll with same start_date




