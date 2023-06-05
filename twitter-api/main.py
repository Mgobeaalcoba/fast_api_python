# Python
from typing import Optional
from enum import Enum
from uuid import UUID # Universal Unique Identified
from datetime import date
# Pydantic
from pydantic import BaseModel
from pydantic import Field, HttpUrl, FilePath, DirectoryPath, EmailStr, PaymentCardNumber, IPvAnyAddress, NegativeFloat, PositiveFloat, NegativeInt, PositiveInt # Function para validar Models
# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, File, UploadFile # Functions para validar Body, Query y Path


# Si usamos el entry point acá el servidor no se levanta. Ojo!!!

app = FastAPI()

# Models:

class Tweet(BaseModel):
    tweet_id: UUID = Field(
        ...,
        example='bd65600d-8669-4903-8a14-af88203add38'
    )

class UserBase(BaseModel):
    user_id: UUID = Field(
        ...,
        example='bd65600d-8669-4903-8a14-af88203add38'
    ) # Universal Unique Identified
    email: EmailStr = Field(
        ...,
        example="gobeamariano@gmail.com"
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(
        default=None
    )

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8
    )

# Home
@app.get(
    path="/",
    )
def home():
    return {"Twitter API": "Working!"}