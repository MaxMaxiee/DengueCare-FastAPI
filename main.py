from fastapi import FastAPI
from db.database import engine
from db import models

app = FastAPI()

@app.get('/testserver')
def index():
    return {
        'message': 'server is working'
    }

models.Base.metadata.create_all(engine)