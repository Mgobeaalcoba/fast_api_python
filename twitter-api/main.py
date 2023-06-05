# Python
from typing import Optional, List
from enum import Enum
from uuid import UUID # Universal Unique Identified
from datetime import date, datetime
import json # Librería del core de Python para trabajar con JSON
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
        ...
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
        min_length=8,
        max_length=64
    )

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
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

## Users

### Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(
    user: UserRegister = Body(...)
):
    """
    Register a User

    This path operation register a user in the app

    Paremeters:
    - Request Body Parameter:
        - user: UserRegister

    Returns:
    - A json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results: List = json.loads(f.read()) # El contenido de f viene en string y lo transformo en lista de dicts con json.loads(). Es lista porque los files json están con "[]" al principio
        user_dict = user.dict() # Convierto el objeto user que recibo en body en un dict.
        # Convierto mis datos UUID y date para no tener errores:
        # Los datos de tipo UUID y date no se convierten a JSON de forma natural
        user_dict["user_id"] = str(user_dict["user_id"]) # Casteo a str
        user_dict["birth_date"] = str(user_dict["birth_date"]) # Casteo a str
        # Agrego a mi lista de diccionarios que me traje del archivo JSON ("base de datos") mi nuevo user:
        results.append(user_dict)
        # Me muevo al primer caracter/byte de mi archivo:
        f.seek(0)
        # Escribo en mi archivo la lista que ya tenía con el nuevo usuario
        f.write(json.dumps(results))
        return user # Retorno el usuario pero sin clave dado el response_model


### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Shows all users",
    tags=["Users"]
)
def show_all_users():
    """
    This path operations shows all users in the app

    Parameters:
    - Without parameters

    Returns:
    - A json list with all user users in the app, with de folloging struct:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

### Show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

### Update a user
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

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show All Tweets",
    tags=["Tweets"]
    )
def home():
    return {"Twitter API": "Working!"}

### Post a Tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"]
)
def post_a_tweet():
    pass

### Show a Tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Delete a Tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a Tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass

