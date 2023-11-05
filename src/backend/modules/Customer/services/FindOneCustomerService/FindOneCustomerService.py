from modules.Customer.repositories.CustomerRepository import CustomerRepository


class FindOneCustomerService():
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, id: int):
        customer = self.repository.find_one(id)

        if customer is None:

            return "Customer not found!"
        else:
            return customer
