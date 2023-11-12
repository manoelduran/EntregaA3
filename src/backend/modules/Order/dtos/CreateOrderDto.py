from pydantic import BaseModel


class CreateOrderDto(BaseModel):
    customer_id: int
    payment_method: str
    product_id: int
    quantity: int

