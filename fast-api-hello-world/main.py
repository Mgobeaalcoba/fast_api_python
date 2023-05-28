# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

# Si usamos el entry point acá el servidor no se levanta. Ojo!!!

app = FastAPI()

# Models:

class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    # Definimos el modelo según "pydantic":
    # caracteristicas o atributos:
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None # Valores opcionales 
    is_married: Optional[str] = None # Valores opcionales


# Path Operations: 1° Path operation
@app.get("/") # Decorador de una función de Python
def home():
    # Las API´s se comunican mediante JSON. En Python JSON es un diccionario...
    return {"Hello": "World"}


# Request and Response Body

@app.post("/person/new")
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
        description="This is the person name. It's between 1 and 50 characters"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required.") # Query Parameter obligatorio... Mala práctica pero puede ocurrir
):
    return {name: age}

# Validaciones: Path Parameters:

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="This is the person ID. It will be greater or equal than cero"
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
        gt=0
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
