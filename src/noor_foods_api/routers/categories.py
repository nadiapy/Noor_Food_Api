from fastapi import APIRouter, HTTPException

from .. import crud
from ..dependencies import SessionDep
from ..models import Category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("")
def list_categories(session: SessionDep) -> list[Category]:
    return crud.list_categories(session)

@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, session: SessionDep):
    category = crud.get_category(session, category_id)
    if category is None:
        raise HTTPException(status_code=404,detail="Category not found")
    return category
