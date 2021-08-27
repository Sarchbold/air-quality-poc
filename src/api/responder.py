from fastapi import FastAPI
from request import *

app = FastAPI()


@app.get("/")
async def return_list(country: str):
    results = getsupportedstates(country)
    if country:
        results.update({"country": country})
    return results
