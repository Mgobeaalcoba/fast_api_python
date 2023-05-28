# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI
from fastapi import Body

# Si usamos el entry point acá el servidor no se levanta. Ojo!!!

app = FastAPI()

# Models:

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
    return Person # Retorno como response lo mismo que recibí como parametro

