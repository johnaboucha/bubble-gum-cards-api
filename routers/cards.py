from fastapi import APIRouter, Depends, HTTPException, status
from data.data import cards
from fastapi.security import OAuth2PasswordBearer
from security.keys import keys

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )

router = APIRouter(prefix="/cards")

@router.get("/")
def read_root():
	return cards[:9]

@router.get("/{id}")
def read_card(id: int):
	for card in cards:
		if id == card["id"]:
			return card
	raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )

@router.put("/{id}", dependencies=[Depends(api_key_auth)])
def update_card(id: int):
	pass

@router.post("/", dependencies=[Depends(api_key_auth)])
def create_card():
	pass

@router.delete("/{id}", dependencies=[Depends(api_key_auth)])
def delete_card(id: int):
	pass