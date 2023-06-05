# Python
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel
from pydantic import Field, HttpUrl, FilePath, DirectoryPath, EmailStr, PaymentCardNumber, IPvAnyAddress, NegativeFloat, PositiveFloat, NegativeInt, PositiveInt, UUID4 # Function para validar Models
# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, File, UploadFile # Functions para validar Body, Query y Path


# Si usamos el entry point acá el servidor no se levanta. Ojo!!!

app = FastAPI()

# Models:

class Tweet(BaseModel):
    tweet_id: UUID4 = Field(
        ...,
        ge=0,
        example=112032
    )

class User(BaseModel):
    user_id: UUID4 = Field(
        ...,
        ge=0,
        example=1712
    ) # Universal Unique Identifiquer

# Home
@app.get(
    path="/",
    )
def home():
    return {"Twitter API": "Working!"}