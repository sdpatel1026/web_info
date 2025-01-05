from pydantic import BaseModel, HttpUrl

class WebInfoRequest(BaseModel):
    url: HttpUrl
