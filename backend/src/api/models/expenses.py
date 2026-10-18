from pydantic import BaseModel
from database.enums import Bill
from database.tables import Expense, ExpenseOverride
from datetime import date
from sqlalchemy import or_

class ExpenseModel(BaseModel):
    id: int
    name: Bill
    amount: float
    start_date: date
    end_date: date | None

class ExpenseFilters(BaseModel):
    name: Bill  | None = None
    start_date: date  | None = None
    end_date: date | None = None

    def apply(self, query):
        if self.name is not None:
            query = query.where(Expense.name == self.name.value)
        if self.start_date is not None:
        # Include expenses that end on/after the filter start date, or are ongoing.
            query = query.where(
                or_(
                    Expense.end_date >= self.start_date,
                    Expense.end_date.is_(None),
                )
            )
        if self.end_date is not None:
            # Expense must have started on/before the filter end date.
            query = query.where(Expense.start_date <= self.end_date)
        return query
    

class ExpenseOverrideModel(BaseModel):
    id: int
    name: Bill
    amount: float
    override_date: date

class ExpenseOverrideFilters(BaseModel):
    name: Bill  | None = None
    start_date: date  | None = None
    end_date: date | None = None

    def apply(self, query):
        if self.name is not None:
            query = query.where(ExpenseOverride.name == self.name.value)
        if self.start_date is not None:
            query = query.where(ExpenseOverride.override_date >= self.start_date)
        if self.end_date is not None:
            query = query.where(ExpenseOverride.override_date <= self.end_date)
        return query
