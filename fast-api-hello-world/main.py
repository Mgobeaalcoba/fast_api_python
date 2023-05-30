# Python
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel
from pydantic import Field, HttpUrl, FilePath, DirectoryPath, EmailStr, PaymentCardNumber, IPvAnyAddress, NegativeFloat, PositiveFloat, NegativeInt, PositiveInt # Function para validar Models
# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path # Functions para validar Body, Query y Path


# Si usamos el entry point acá el servidor no se levanta. Ojo!!!

app = FastAPI()

# Models:

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=20,
        example="Ituzaingo"
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=20,
        example="Buenos Aires"
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=20,
        example="Argentina"
    )
    
# Limpió mis lineas repetidas de codigo entre person y person out
# aplicando la herencia: 

# Class Person Base para limpiar codigo y luego aplicar herencia:
class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Nicole"
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Ferandez"
    )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=29
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example="Blonde"
    ) # Valores opcionales 
    is_married: Optional[bool] = Field(
        default=None,
        example=True
    )

class Person(PersonBase):
    # Solo agrego el password dado que los demas atributos ya me 
    # vienen de PersonBase
    # Manejo de contraseñas:
    # 1- Jamas devolver la contraseña al cliente en el response. Solución: Response Model
    # 2- Jamas almacenar la contraseña como texto plano sino como hash
    password: str = Field(
        ...,
        min_length=8
    )
    # Sub-Clase Config que define valore por defecto solo al servicio
    # de probar nuestra API
    # class Config:
    #     screma_extra = {
    #         "example": {
    #             "first_name": "Mariano",
    #             "last_name": "Gobea Alcoba",
    #             "age": 35,
    #             "hair_color": "Blonde",
    #             "is_married": False
    #         }
    #     }

class PersonOut(PersonBase):
    # Pongo un pass porque todos los atributos de PersonOut ya
    # me vienen de PersonBase
    pass

# Path Operations: 1° Path operation
@app.get("/") # Decorador de una función de Python
def home():
    # Las API´s se comunican mediante JSON. En Python JSON es un diccionario...
    return {"Hello": "World"}


# Request and Response Body
# Al declarar un response model en mi decorator no necesito modificar la variable que retorno en mi func.

@app.post("/person/new", response_model=PersonOut)
def create_person(person: Person = Body(...)): # Los "..." en Body indican que el Body es obligatorio
    return person # Retorno como response lo mismo que recibí como parametro

# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        example="Mariano"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required."), # Query Parameter obligatorio... Mala práctica pero puede ocurrir
        example=25
):
    return {name: age}

# Validaciones: Path Parameters:

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="This is the person ID. It will be greater or equal than cero",
        example=123
        ) # Como es un path parameters debe ser obligatorio
):
    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0,
        example=123
    ),
    person: Person = Body(
        ...,
    ),
    location: Location = Body(
        ...,
    )
):
    # Voy a combinar el JSON/Diccionario person con el 
    # JSON/Diccionario location en una sola variable. 
    # Para luego retornarla
    results = person.dict()
    results.update(location.dict())
    return results
