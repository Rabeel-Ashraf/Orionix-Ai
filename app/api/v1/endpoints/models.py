from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_models():
    return {"message": "Models endpoint working!"}
