from pydantic import BaseModel
from database.enums import Bill
from datetime import date

class ExpenseModel(BaseModel):
    name: Bill
    amount: float
    start_date: date
    end_date: date | None

class ExpenseOverrideModel(BaseModel):
    name: Bill
    amount: float
    override_date: date