from fastapi import FastAPI

# Si usamos el entry point acá el servidor no se levanta. Ojo!!!

app = FastAPI()

        # Path Operations: 1° Path operation
@app.get("/") # Decorador de una función de Python
def home():
    # Las API´s se comunican mediante JSON. En Python JSON es un diccionario...
    return {"Hello": "World"}

