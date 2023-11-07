from modules.Order.dtos.UpdateOrderDto import UpdateOrderDto
from modules.Order.repositories.OrderRepository import OrderRepository


class UpdateOrderService():
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, id: int, order: UpdateOrderDto):
        foundOrder = self.repository.find_one(id)
        if foundOrder is None:
            return "Order not found!"
        else:
            updatedOrder = self.repository.update(id, order)
            return updatedOrder
