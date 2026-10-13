from pydantic import BaseModel
from database.enums import Bill
from datetime import date

class ExpenseModel(BaseModel):
    name: Bill
    amount: float
    start_date: date
    end_date: date | None
    one_off: bool

class CurrentOngoingExpense(BaseModel):
    name: Bill
    amount: float