# Python
from typing import Optional, List
from enum import Enum
from uuid import UUID # Universal Unique Identified
from datetime import date, datetime
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

class Tweet(BaseModel):
    tweet_id: UUID = Field(
        ...,
        example='bd65600d-8669-4903-8a14-af88203add38'
    )
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
    )
    created_at: date = Field(
        default=datetime.now()
    )
    updated_at: Optional[date] = Field(
        default=None
    )
    by: User = Field(
        ...
    )

# Path Operations

## Home

@app.get(
    path="/",
    )
def home():
    return {"Twitter API": "Working!"}

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Shows all users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass

## Tweets

