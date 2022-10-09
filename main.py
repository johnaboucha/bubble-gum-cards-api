from fastapi import FastAPI
from data.cards import cards

app = FastAPI()

@app.get("/")
def root():
	return {"message":cards[:9]}