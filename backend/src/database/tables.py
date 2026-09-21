from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database.enums import Role
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
    amount: Mapped[float] = mapped_column() # Can be # or %.

    expense_id: Mapped[int] = mapped_column(ForeignKey("expense.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped[User] = relationship()


class Expense(Base):
    __tablename__ = "expense"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    amount: Mapped[float] = mapped_column()
    start_date: Mapped[date] = mapped_column()
    end_date: Mapped[date | None] = mapped_column()

    splits: Mapped[list[Split]] = relationship()


