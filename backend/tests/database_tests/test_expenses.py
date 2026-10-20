from datetime import date

from household_service.database.tables import Expense, ExpenseOverride
from household_service.database.enums import Bill


def test_expense_and_overrides(session):
    expense = Expense(
        name=Bill.rent,
        amount=100.0,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
        overrides=[
            ExpenseOverride(
                name=Bill.rent,
                amount=120.0,
                override_date=date(2026, 2, 1),
            )
        ],
    )
    session.add(expense)
    session.commit()
    saved_expense = session.get(Expense, expense.id)
    assert saved_expense is not None
    assert len(saved_expense.overrides) == 1