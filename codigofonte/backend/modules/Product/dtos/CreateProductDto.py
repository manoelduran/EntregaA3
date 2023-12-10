from pydantic import BaseModel


class CreateProductDto(BaseModel):
    name: str
    price: int
    quantity: int
