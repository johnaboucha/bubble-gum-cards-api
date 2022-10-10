from fastapi import APIRouter

router = APIRouter(prefix="/players")

@router.get("/")
def read_root():
	return {"message":"player list"}

@router.put("/{id")
def update_card(id: int):
	pass

@router.post("/")
def create_card():
	pass

@router.delete("/?id={id}")
def delete_card(id: int):
	pass