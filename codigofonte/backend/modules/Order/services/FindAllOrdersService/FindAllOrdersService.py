from modules.Order.repositories.OrderRepository import OrderRepository


class FindAllOrdersService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self):
        return self.repository.find_all()
