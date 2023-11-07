from modules.Customer.dtos.CreateCustomerDto import CreateCustomerDto
from modules.Customer.repositories.CustomerRepository import CustomerRepository


class CreateCustomerService():
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer: CreateCustomerDto):
        foundCustomer = self.repository.find_by_email(
            email=customer.email)
        if foundCustomer is CreateCustomerDto:
            return "Already exists an user with this email!"
        else:
            newCustomer = self.repository.create(customer=customer)
            return newCustomer
