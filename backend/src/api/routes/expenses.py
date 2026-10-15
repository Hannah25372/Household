from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from database.database import get_db
from database.tables import Expense, ExpenseOverride
from api.models.expenses import ExpenseModel, ExpenseOverrideModel
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

@router.get("/override", response_model=PaginatedResponse[ExpenseOverrideModel])
def list_overrides(
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    total = db.query(ExpenseOverride).count()
    overrides = (
        db.query(ExpenseOverride)
        .offset(pagination.offset)
        .limit(pagination.page_size)
        .all()
    )
    return {
        "items": overrides,
        "page": pagination.page,
        "page_size": pagination.page_size,
        "total": total,
    }

@router.get("/current", response_model=list[ExpenseModel])
def get_current_expenses(
    db: Session = Depends(get_db),
):
    stmt = (
        select(Expense)
        .where(Expense.end_date.is_(None))
        )
    expenses = db.execute(stmt).all()
    return [
        ExpenseModel.model_validate(expense)
        for expense in expenses
        ]


# TODO: Routes: add ongoing / modify ongoing / add override / modify override