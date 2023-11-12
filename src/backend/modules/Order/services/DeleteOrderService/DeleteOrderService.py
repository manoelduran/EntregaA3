from modules.Order.repositories.OrderRepository import OrderRepository
from modules.Product.repositories.ProductRepository import ProductRepository


class DeleteOrderService():
    def __init__(self, repository: OrderRepository, product_repository: ProductRepository):
        self.repository = repository
        self.product_repository = product_repository

    def execute(self, id: int):
        order = self.repository.find_one(id)
        if order is None:
            return "Order not found!"
        self.repository.delete(id)
        return order
