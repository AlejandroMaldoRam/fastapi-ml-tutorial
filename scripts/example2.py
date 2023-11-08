# This script uses parameters in the URL
from fastapi import FastAPI

app = FastAPI()

# See what happen when you give 2, 3.4, hello as parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}