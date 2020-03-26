from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"greeting": "Hello, IM."}


@app.get('/lang')
async def read_root():
    return {
        "people": "IM",
        "lang": ["Python", "Elixir", "PHP"]
        }


@app.get('/items/{item_id}')
async def read_item(item_id: int, query: str = None):
    return {
        "item_id": item_id,
        "query": query}
