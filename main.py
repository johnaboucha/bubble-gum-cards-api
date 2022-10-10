from fastapi import FastAPI
from routers import cards, manufacturers, players

app = FastAPI()

app.include_router(cards.router)
app.include_router(players.router)
app.include_router(manufacturers.router)