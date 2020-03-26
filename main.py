from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"greeting": "Hello, IM."}

@app.get('/lang')
async def read_root():
    return {
        "people": "IM",
        "lang": ["Python", "Elixir", "PHP"]
        }