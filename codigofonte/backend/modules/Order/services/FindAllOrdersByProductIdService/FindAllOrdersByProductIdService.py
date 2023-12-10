from modules.Order.repositories.OrderRepository import OrderRepository


class FindAllOrdersByProductIdService():
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, product_id: int):
        orders = self.repository.find_all_by_product_id(product_id)

        if orders is None:

            return "This product was never sold! :("
        else:
            return orders
