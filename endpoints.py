from fastapi import FastAPI, responses
from functions import *
from pydantic import BaseModel
from datetime import date
from predireTirageGagnant import *



class Row(BaseModel):
        date: date
        n1: int
        n2: int
        n3: int
        n4: int
        n5: int
        e1: int
        e2: int
        win: int
        gain: int

app = FastAPI()


@app.get('/')
async def root():
    return {"message" : "Best app ever !"}


@app.get('/predict')
async def predictionGet():
    message = {'Success' : 'Voci votre prédiction : n1 : \n n2 : \n n3 : \n n4 : \n n5 : \n e1 : \n e2 : '}
    return responses.JSONResponse(content = message,status_code=201)

@app.post('/predict')
async def predictionPost(n1: int, n2: int, n3: int, n4: int, n5: int, e1: int, e2: int):
    res = predireTirageProbaGagnant(n1,n2,n3,n4,n5,e1,e2)
    message = {'Success' : 'Probabilité que le tirage soit gagnant : ' + str(res)}
    return responses.JSONResponse(content = message,status_code=201)

@app.get('/model')
async def modelGet():
    return {"message" : "pas encore implementé"}

@app.post('/model')
async def modelPost():
    # Ajouter l'appel fonctions model
    return responses.JSONResponse(content = {'Success' : 'Le modele vient d\'être restart'},status_code=201)

@app.put('/model', status_code=201)
async def add_row(date: date, n1: int, n2: int, n3: int, n4: int, n5: int, e1: int, e2: int, win: int, gain: int):
    addData(date,n1,n2,n3,n4,n5,e1,e2,win,gain)
    return responses.JSONResponse(content = {'Success' : 'Données bien ajoutée au csv'},status_code=201)


