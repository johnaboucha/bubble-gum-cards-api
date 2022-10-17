from fastapi import APIRouter, Depends, HTTPException, status
from data.sheets import cards
from security.keys import api_key_auth, keys

router = APIRouter(prefix="/api/cards")

@router.get("/")
def read_root(skip: int = 0, top: int = 9, search: str = None, category: str = None):
	if search != None and category == None:
		results = []
		for card in cards:
			card_contents = card["player"] + card["description"]
			if search.lower() in card_contents.lower():
				results.append(card)
		return results[skip:skip+top]
	elif search != None and category != None:
		results = []
		for card in cards:
			card_contents = card["player"] + card["description"]
			if search.lower() in card_contents.lower() and category.lower() == card["category"].lower():
				results.append(card)
		return results[skip:skip+top]
	elif category != None:
		results = []
		for card in cards:
			if category.lower() == card["category"].lower():
				results.append(card)
		return results[skip:skip+top]

	return cards[skip:skip+top]

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

@router.get("/sheets/")
def read_root2():
	pass