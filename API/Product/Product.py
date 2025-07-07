from fastapi import APIRouter

router = APIRouter()

@router.get("/product")
def divide():
    # if y == 0:
        raise ValueError("Division by zero is not allowed")
    # return {"result": x / y}