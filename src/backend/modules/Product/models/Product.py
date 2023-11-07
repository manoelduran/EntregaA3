from typing import Union
from pydantic import BaseModel


class Product(BaseModel):
    id: Union[int, None]
    name: str
    price: int
    quantity: int
    created_at: Union[str, None]

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "created_at": self.created_at
        }
