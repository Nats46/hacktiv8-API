from fastapi import FastAPI, HTTPException 
import pandas as pd
import http

app = FastAPI()

@app.get("/")
def HelloWorld():
    return {"msg": "hello World"}

@app.get("/lalalal")
def HelloWorld():
    return {"msg": "lalalal"}

@app.get("/klonting")
def HelloWorld():
    return {"msg": "klontong"}

@app.get("/data_csv")
def ReadCsv():
    df = pd.read_csv("mock-employees.csv")

    df = df.to_dict(orient='records')

    return {
        "data":df
    }

@app.get("/data/{id}")
def HandleFilter(id: int):
    df = pd.read_csv("mock-employees.csv")

    df = df[df['id']==id]
    # df = df.query(f"id == {id}")

    if df.empty:
        raise HTTPException(status_code=400, detail=f"Employee {id} not found")
        
    df = df.to_dict(orient='records')

    return {
        "data":df
    }