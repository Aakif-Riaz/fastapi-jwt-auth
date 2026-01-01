from fastapi import APIRouter, Depends
from models import User
from auth.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }
