from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# All the params defined in the Python function 
# that are not in the param string are taken as query parameters
# Usage: 
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# An API for doing a sum of two query parameters
@app.get("/sum/")
async def sum_values(a: int=0, b: int=0):
    return {"result":a+b}