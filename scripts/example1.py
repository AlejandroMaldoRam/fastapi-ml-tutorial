"""
Basic example of FastAPI.
1. Run uvicorn example1:app --reload
2. Open the http://127.0.0.1:8000 on a browser.
3. FastAPI creates a documentation page in http://127.0.0.1:8000/docs
"""

# Import libraries
from fastapi import FastAPI

# Instance the app (intermediary) to use FastAPI
app = FastAPI()

# Define functions to respond the requests.
@app.get("/")
async def root():
    # This will return a JSON with this information.
    return {"message": "Hello world"} 
