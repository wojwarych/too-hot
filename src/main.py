from fastapi import FastAPI

from db import db
from models import Sequence


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/sequences/")
async def list_sequences():
    sequences = []
    for seq in db.sequences.find():
        sequences.append(Sequence(**seq))
    return sequences


@app.post("/sequences/", status_code=201)
async def insert_sequence(sequence: Sequence):
    if hasattr(sequence, "id"):
        delattr(sequence, "id")
    ret = db.sequences.insert_one(sequence.dict(by_alias=True))
    return sequence.dict()
