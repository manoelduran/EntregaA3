from modules.Customer.repositories.CustomerRepository import CustomerRepository


class FindAllCustomersService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self):
        return self.repository.find_all()
