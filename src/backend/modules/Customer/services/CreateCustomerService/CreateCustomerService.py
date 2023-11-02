from modules.Customer.repositories.CustomerRepository import CustomerRepository

class CreateCustomerService():
    def __init__(self, customerRepository: CustomerRepository):
        self.customerRepository = customerRepository
    def execute(self):
        customers = self.customerRepository.create()
        return customers
