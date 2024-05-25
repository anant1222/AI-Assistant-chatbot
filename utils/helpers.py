# utils/helpers.py
from app.models.response import APIResponse

def format_response(status: str, message: str, data: Any = None) -> APIResponse:
    return APIResponse(status=status, message=message, data=data)
