from modules.Customer.models.Customer import Customer
from modules.Customer.repositories.CustomerRepository import CustomerRepository


class UpdateCustomerService():
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, id: int, customer: Customer):
        foundCustomer = self.repository.find_one(id)
        if foundCustomer is None:
            return "Customer not found!"
        else:
            updatedCustomer = self.repository.update(id, customer)
            return updatedCustomer
