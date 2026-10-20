from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UniqueConstraint, Index, CheckConstraint, or_, ForeignKey
from household_service.database.enums import Role, Bill
from datetime import date

from household_service.database.database import Base

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

    overrides: Mapped[list["ExpenseOverride"]] = relationship(back_populates="expense")

    __table_args__ = (
        CheckConstraint(
            or_(
                end_date.is_(None),
                end_date >= start_date
            ),
            name="ck_valid_date_range",
        ),
        Index(
        "uq_bill_name_open_ended",
        "name",
        unique=True,
        sqlite_where=end_date.is_(None),
    ),
    )

    # Constraint: cannot have overlapping dates in the same Bill
    #Also add trigger for override date between start and end date

class ExpenseOverride(Base):
    __tablename__ = "expense_override"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Bill] = mapped_column()
    amount: Mapped[float] = mapped_column()
    override_date: Mapped[date] = mapped_column()

    expense_id: Mapped[int] = mapped_column(ForeignKey("expense.id"))
    expense: Mapped["Expense"] = relationship(back_populates="overrides")

    __table_args__ = (
        UniqueConstraint("override_date", "name", name="uq_override_date_name"),
    )




