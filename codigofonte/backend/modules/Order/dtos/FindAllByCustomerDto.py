from typing import Union
from pydantic import BaseModel


class FindAllByCustomerDto(BaseModel):
    id: Union[int, None]
    customer_id: int
    product_id: int
    quantity: int
    product_name: str
    price: int
    ordered_at: Union[str, None]
