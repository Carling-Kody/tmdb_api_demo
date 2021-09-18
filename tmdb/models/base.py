from pydantic import BaseModel


class GenericResponse(BaseModel):
    status_code: int
    status_message: str
