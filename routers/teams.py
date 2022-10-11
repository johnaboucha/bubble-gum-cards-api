from fastapi import APIRouter, HTTPException, status
from data.data import teams

router = APIRouter(prefix="/api/teams")

@router.get("/")
def read_root(skip: int = 0, limit: int = 10, search: str = None):
	if search != None:
		results = []
		for team in teams:
			search_text = team["location"] + " " + team["name"]
			if search.lower() in search_text.lower():
				results.append(team)
		return results[skip:skip+limit]
	return teams[skip:skip+limit]

@router.get("/{id}")
def read_team(id: int):
	for team in teams:
		if id == team["id"]:
			return team
	raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )

@router.put("/{id")
def update_team(id: int):
	pass

@router.post("/")
def create_team():
	pass

@router.delete("/?id={id}")
def delete_team(id: int):
	pass