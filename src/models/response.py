from pydantic import BaseModel
from typing import Optional

class WebInfoResponse(BaseModel):
    industry: Optional[str]
    company_size: Optional[str]
    location: Optional[str]
