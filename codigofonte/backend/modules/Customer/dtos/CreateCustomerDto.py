from pydantic import BaseModel


class CreateCustomerDto(BaseModel):
    name: str
    email: str
    password: str
