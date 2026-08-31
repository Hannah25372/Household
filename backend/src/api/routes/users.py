from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User
from api.models.users import UserCreate, UserResponse
from api.pagination import PaginationParams, PaginatedResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user


@router.get("/", response_model=PaginatedResponse[UserResponse])
def list_users(
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    total = db.query(User).count()
    users = (
        db.query(User)
        .offset(pagination.offset)
        .limit(pagination.page_size)
        .all()
    )
    return {
        "items": users,
        "page": pagination.page,
        "page_size": pagination.page_size,
        "total": total,
    }


@router.post("/", response_model=UserResponse)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}