from app.database import Base, engine
from app.models import Author as ModelAuthor
from app.models import Book as ModelBook
from app.schema import Author as SchemaAuthor
from app.schema import Book as SchemaBook
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}
