from pydantic import BaseModel, ValidationError, conint, validator, PydanticValueError
from uuid import UUID
from typing import List, Optional


class Student(BaseModel):
    """Student model for students"""
    id: str | UUID
    first_name: str
    last_name: str
    username: str
    age: conint(ge=16)
    email: str
    carreers: list[str]

    @validator('carreers')
    def must_have_carreers(cls, value):
        if value is None or len(value) < 1:
            raise NoCarreersException(err='No carreers included!')
        return value # Value must be return to be mapped 
    
class NoCarreersException(PydanticValueError):
    code = 'NO_CARREER_ERR'
    msg_template = 'ERROR: Carreers validation error, message: "{err}"'