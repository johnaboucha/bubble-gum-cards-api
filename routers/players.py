from fastapi import APIRouter
from data.data import players

router = APIRouter(prefix="/api/players")

@router.get("/")
def read_root(skip: int = 0, limit: int = 10):
	return players[skip:skip+limit]

@router.put("/{id")
def update_card(id: int):
	pass

@router.post("/")
def create_card():
	pass

@router.delete("/?id={id}")
def delete_card(id: int):
	pass