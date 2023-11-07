from modules.Order.dtos.CreateOrderDto import CreateOrderDto
from modules.Order.repositories.OrderRepository import OrderRepository


class CreateOrderService():
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order: CreateOrderDto):
        foundOrder = self.repository.find_one(
            id=order.customer_id)
        if foundOrder is CreateOrderDto:
            return "Already exists an order with this customer_id!"
        else:
            newOrder = self.repository.create(order=order)
            return newOrder
