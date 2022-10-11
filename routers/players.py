from fastapi import APIRouter, Depends, HTTPException, status
from security.keys import api_key_auth, keys
from data.data import players

router = APIRouter(prefix="/api/players")

@router.get("/")
def read_root(skip: int = 0, limit: int = 10, search: str = None):
	if search != None:
		results = []
		for player in players:
			search_text = player["first_name"] + " " + player["last_name"]
			if search.lower() in search_text.lower():
				results.append(player)
		return results[skip:skip+limit]
	return players[skip:skip+limit]

@router.get("/{id}")
def read_player(id:int):
	for player in players:
		if id == player["id"]:
			return player
	raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )

@router.put("/{id")
def update_player(id: int, dependencies=[Depends(api_key_auth)]):
	pass

@router.post("/")
def create_player(dependencies=[Depends(api_key_auth)]):
	pass

@router.delete("/?id={id}")
def delete_player(id: int, dependencies=[Depends(api_key_auth)]):
	pass