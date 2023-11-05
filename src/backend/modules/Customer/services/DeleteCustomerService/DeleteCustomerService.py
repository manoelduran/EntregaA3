from modules.Customer.repositories.CustomerRepository import CustomerRepository


class DeleteCustomerService():
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, id: int):
        customer = self.repository.find_one(id)

        if customer is None:

            return "Customer not found!"
        else:
            self.repository.delete(id)
            return customer
