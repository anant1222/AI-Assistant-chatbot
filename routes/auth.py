from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str):
    return {"message": "Login successful"}

@router.post("/logout")
async def logout():
    return {"message": "Logout successful"}