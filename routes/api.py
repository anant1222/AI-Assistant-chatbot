from fastapi import APIRouter, Depends
from routes_model.user import User
from utils.helpers import format_response
from routes_model.response import APIResponse

router = APIRouter()

@router.post("/query", response_model=APIResponse)
async def query_endpoint(query: str):
    response = handle_query(query)
    return format_response(status="success", message="Query processed successfully", data={"response": response})