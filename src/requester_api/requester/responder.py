from fastapi import FastAPI
from request import Requester

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Execute query by adding /countries/?country=usa"}


@app.get("/countries/")
async def return_list(country: str):
    results = Requester(country)
    return results
