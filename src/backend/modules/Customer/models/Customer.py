from typing import Optional
from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    email: str
    password: str

    def json(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
