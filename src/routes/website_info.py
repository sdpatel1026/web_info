from fastapi import APIRouter, Depends,HTTPException,status
from src.models.request import WebInfoRequest
from src.models.response import WebInfoResponse
from src.services.web_info import web_info as fetch_web_info 
from src.services.auth import authenticate
from src.config import config
import logging
logging.basicConfig(level=logging.ERROR)

router = APIRouter()

@router.post("/website_info", response_model=WebInfoResponse)
def web_info(
    req: WebInfoRequest, authenticated_user: dict = Depends(authenticate)
):
    try:
        result = fetch_web_info(req.url)
        return WebInfoResponse(**result)
    except Exception as e:
        logging.error(f"Error in analyze_content: {e}", exc_info=True)
       
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong at the server side. Please try again later...")
