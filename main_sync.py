from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    a: int
    b: str


app = FastAPI()


@app.post("/echo_json/")
def echo_json(item: Item):
    return item
