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


class Expense(Base):
    __tablename__ = "expense"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Bill] = mapped_column()
    amount: Mapped[float] = mapped_column()
    start_date: Mapped[date] = mapped_column()
    end_date: Mapped[date | None] = mapped_column()

    # Constraints:
    # - Can only have one of each Bill with end_date None
    # - Cannot have overlapping dates in the same Bill

class ExpenseOverride(Base):
    __tablename__ = "expense_override"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Bill] = mapped_column()
    amount: Mapped[float] = mapped_column()
    override_date: Mapped[date] = mapped_column()

    # Constraints:
        # - Cannot have multiple Bill with same override_date




