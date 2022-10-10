from fastapi import APIRouter
from data.data import teams

router = APIRouter(prefix="/api/teams")

@router.get("/")
def read_root(skip: int = 0, limit: int = 10):
	return teams[skip:skip+limit]

@router.put("/{id")
def update_team(id: int):
	pass

@router.post("/")
def create_team():
	pass

@router.delete("/?id={id}")
def delete_team(id: int):
	pass