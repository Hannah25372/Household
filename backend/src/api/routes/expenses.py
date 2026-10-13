from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from database.database import get_db
from database.tables import Expense
from api.models.expenses import ExpenseModel, CurrentOngoingExpense
from api.pagination import PaginationParams, PaginatedResponse

router = APIRouter(prefix="/expenses", tags=["Expenses"])

#TODO: add filters for bill, date range, one off
@router.get("/", response_model=PaginatedResponse[ExpenseModel])
def list_expenses(
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    total = db.query(Expense).count()
    expenses = (
        db.query(Expense)
        .offset(pagination.offset)
        .limit(pagination.page_size)
        .all()
    )
    return {
        "items": expenses,
        "page": pagination.page,
        "page_size": pagination.page_size,
        "total": total,
    }

@router.get("/current", response_model=list[CurrentOngoingExpense])
def get_current_ongoing_expenses(
    db: Session = Depends(get_db),
):
    stmt = (
        select(Expense.name, Expense.amount)
        .where(Expense.end_date.is_(None), Expense.one_off.is_(False))
        )
    expenses = db.execute(stmt).all()
    return [
        CurrentOngoingExpense(name=name, amount=amount)
        for name, amount in expenses
        ]


# TODO: Routes: add ongoing / modify ongoing / add one off / modify one off