# pydantic models. validation layers
from pydantic import BaseModel, field_validator, EmailStr, Field
from typing import Optional


class UserSignup(BaseModel):
    username: str = Field(min_length=2, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8)
    age: Optional[int] = Field(default=None, ge=16, le=40)

    @field_validator("username")
    def strip_username(
        cls, v
    ):  # cls refers to the model class itself (in this case UserSignup , v is actual value of username i.e for which decorator is run)
        return v.strip()

    @field_validator("password")
    def strong_password(cls, v):
        if " " in v:
            raise ValueError("Password cannot contain spaces")
        return v
