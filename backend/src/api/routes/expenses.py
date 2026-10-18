from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from database.database import get_db
from database.tables import Expense, ExpenseOverride
from api.models.expenses import ExpenseModel, ExpenseOverrideModel, ExpenseFilters, ExpenseOverrideFilters
from api.pagination import PaginationParams, PaginatedResponse

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.get("/", response_model=PaginatedResponse[ExpenseModel])
def list_expenses(
    pagination: PaginationParams = Depends(),
    filters: ExpenseFilters = Depends(),
    db: Session = Depends(get_db),
):
    query = db.select(Expense)
    query = filters.apply(query)
    count_query = select(func.count()).select_from(
        query.order_by(None).subquery()
    )
    total = db.scalar(count_query)
    query = query.order_by(Expense.start_date.desc())
    query = query.offset(pagination.offset).limit(pagination.page_size)
    expenses = db.scalars(query).all()

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
    expense_data: ExpenseModel,
    db: Session = Depends(get_db),
):
    expense = db.get(Expense, id)
    if expense is None:
        raise HTTPException(status_code=404,detail="Expense not found")
    expense.amount = expense_data.amount
    expense.start_date = expense_data.start_date
    expense.end_date = expense_data.end_date
    db.commit()
    db.refresh(expense)
    return expense

@router.delete("/{id}")
def delete_expense(
    id: int,
    db: Session = Depends(get_db),
):
    expense = db.get(Expense, id)
    if expense is None:
        raise HTTPException(status_code=404,detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted"}

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
    override_data: ExpenseOverrideModel,
    db: Session = Depends(get_db),
):
    override = db.get(ExpenseOverride, id)
    if override is None:
        raise HTTPException(status_code=404,detail="Override not found")
    override.amount = override_data.amount
    db.commit()
    db.refresh(override)
    return override

@router.delete("/override/{id}")
def delete_override(
    id: int,
    db: Session = Depends(get_db),
):
    override = db.get(ExpenseOverride, id)
    if override is None:
        raise HTTPException(status_code=404,detail="Override not found")
    db.delete(override)
    db.commit()
    return {"message": "Override deleted"}