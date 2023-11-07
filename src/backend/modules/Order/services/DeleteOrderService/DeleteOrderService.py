from modules.Order.repositories.OrderRepository import OrderRepository


class DeleteOrderService():
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, id: int):
        order = self.repository.find_one(id)

        if order is None:

            return "Order not found!"
        else:
            self.repository.delete(id)
            return order
