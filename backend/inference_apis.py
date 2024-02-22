from fastapi import HTTPException, APIRouter


inference_router = APIRouter()


@inference_router.get("/test/")
async def test():
    return {"message": "Test GET call From Inference APIs"}
