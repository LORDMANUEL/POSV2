from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict, Any

# Role Schemas
class RoleBase(BaseModel):
    name: str
    permissions: Dict[str, Any]

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

# Branch Schemas
class BranchBase(BaseModel):
    name: str
    location: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None

class BranchCreate(BranchBase):
    pass

class BranchUpdate(BranchBase):
    pass

class Branch(BranchBase):
    id: int

    class Config:
        orm_mode = True

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role_id: int
    branch_id: Optional[int] = None

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role_id: Optional[int] = None
    branch_id: Optional[int] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int
    is_active: bool
    role: Role
    branch: Optional[Branch] = None

    class Config:
        orm_mode = True

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
