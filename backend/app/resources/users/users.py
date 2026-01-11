from enum import Enum
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime

class SystemPermissionLevel(Enum):
    user = "user"
    admin = "admin"
    
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str
    permission: SystemPermissionLevel = Field(default=SystemPermissionLevel.user)
    created_at: datetime | None = Field(default = datetime.now())
    updated_at: datetime = Field(default = datetime.now())
    disabled_at: datetime | None = None
    
class UserCreate(BaseModel):
    name: str
    password: str

class UserUpdate(BaseModel):
    password: str | None = None