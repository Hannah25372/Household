from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from database.database import get_db
from database.tables import Expense, ExpenseOverride
from api.models.expenses import ExpenseModel, ExpenseOverrideModel
from api.pagination import PaginationParams, PaginatedResponse

router = APIRouter(prefix="/expenses", tags=["Expenses"])


#TODO: add filters for bill, date range
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
def list_current_expenses(
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

@router.post("/", response_model=ExpenseModel)
def create_expense(
        expense_data: ExpenseModel,
        db: Session = Depends(get_db),
    ):
    expense = Expense(
            name=expense_data.name,
            amount=expense_data.amount,
            start_date=expense_data.start_date,
            end_date=expense_data.end_date
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

@router.post("/{id}", response_model=ExpenseModel)
def update_expense(
    id: int,
    db: Session = Depends(get_db),
):
    return

@router.post("/override", response_model=ExpenseOverrideModel)
def create_override(
    override_data: ExpenseOverrideModel,
    db: Session = Depends(get_db),
):
    override = ExpenseOverride(
        name=override_data.name,
        amount=override_data.amount,
        override_date=override_data.override_date,
    )
    db.add(override)
    db.commit()
    db.refresh(override)
    return override

@router.post("/override/{id}", response_model=ExpenseOverrideModel)
def update_override(
    id: int,
    db: Session = Depends(get_db),
):
    return