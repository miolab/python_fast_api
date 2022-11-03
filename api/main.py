from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get('/hello')
async def hello():
    return {"message": "Hello, world!"}


@app.get('/')
def read_root():
    return {"greeting": "Hello, root."}


@app.get('/lang')
async def read_root():
    return {
        "people": "IM",
        "lang": ["Python", "Elixir", "Go"]
    }


@app.get('/items/{item_id}')
async def read_item(item_id: int, query: str = None):
    return {
        "item_id": item_id,
        "query": query
    }


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_id": item_id
    }
