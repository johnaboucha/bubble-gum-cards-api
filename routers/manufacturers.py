from fastapi import APIRouter
from data.data import manufacturers

router = APIRouter(prefix="/manufacturers")

@router.get("/")
def read_root():
	return manufacturers[:9]

@router.put("/{id")
def update_card(id: int):
	pass

@router.post("/")
def create_card():
	pass

@router.delete("/?id={id}")
def delete_card(id: int):
	pass