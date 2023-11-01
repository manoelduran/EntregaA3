from modules.Customer.repositories.CustomerRepository import CustomerRepository
from fastapi import HTTPException

class FindOneCustomerService():
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, id: int):
        customer = self.repository.find_one(id)
        if customer is None:
           raise HTTPException(status_code=404, detail="Customer not found!")
        return customer