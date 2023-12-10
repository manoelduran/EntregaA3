from typing import Union
from pydantic import BaseModel


class Order(BaseModel):
    id: Union[int, None]
    customer_id: int
    payment_method: str
    product_id: int
    quantity: int
    ordered_at: Union[str, None]

    def json(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "payment_method": self.payment_method,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "ordered_at": self.ordered_at
        }
