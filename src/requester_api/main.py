from fastapi import FastAPI
from requester_api.requester import Request


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Execute query by adding /countries/?country=usa"}


@app.get("/countries/")
async def return_list(country: str):
    results = Request(country)
    return results.getsupportedstates()

