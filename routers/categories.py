from fastapi import APIRouter, Depends, HTTPException, status
from security.keys import api_key_auth, keys
from data.data import categories

router = APIRouter(prefix="/api/categories")

@router.get("/")
def read_root(skip: int = 0, top: int = 9, search: str = None):
	return {"categories": categories}