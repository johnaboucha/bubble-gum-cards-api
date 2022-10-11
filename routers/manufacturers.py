from fastapi import APIRouter, Depends, HTTPException, status
from data.data import manufacturers
from security.keys import api_key_auth, keys

router = APIRouter(prefix="/api/manufacturers")

@router.get("/")
def read_root(skip: int = 0, limit: int = 10, search: str = None):
	if search != None:
		results = []
		for m in manufacturers:
			if search.lower() in m["name"].lower():
				results.append(m)
		return results[skip:skip+limit]

	return manufacturers[skip:skip+limit]

@router.get("/{id}")
def read_manufacturer(id: int):
	for m in manufacturers:
		if id == m["id"]:
			return m
	raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found"
        )

@router.put("/{id")
def update_manufacturer(id: int, dependencies=[Depends(api_key_auth)]):
	pass

@router.post("/")
def create_manufacturer(dependencies=[Depends(api_key_auth)]):
	pass

@router.delete("/?id={id}")
def delete_manufacturer(id: int, dependencies=[Depends(api_key_auth)]):
	pass