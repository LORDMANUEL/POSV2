from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.auth import security
from core.auth.dependencies import get_current_user, require_role
from . import schemas, services, models

router = APIRouter()

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = services.authenticate_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/users", response_model=schemas.User, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Admin"))])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db=db, user=user)

@router.get("/users/me", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.get("/users", response_model=List[schemas.User], dependencies=[Depends(require_role("Admin"))])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@router.post("/roles", response_model=schemas.Role, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Admin"))])
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return services.create_role(db, role)

@router.post("/branches", response_model=schemas.Branch, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Admin"))])
def create_branch(branch: schemas.BranchCreate, db: Session = Depends(get_db)):
    return services.create_branch(db, branch)
