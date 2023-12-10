from typing import Union
from pydantic import BaseModel


class Customer(BaseModel):
    id: Union[int, None]
    name: str
    email: str
    password: str
    created_at: Union[str, None]

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at
        }
