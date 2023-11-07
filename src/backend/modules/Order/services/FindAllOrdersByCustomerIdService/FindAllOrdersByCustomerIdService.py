from modules.Order.repositories.OrderRepository import OrderRepository


class FindAllOrdersByCustomerIdService():
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, customer_id: int):
        orders = self.repository.find_all_by_customer_id(customer_id)

        if orders is None:

            return "This customer never bought before!"
        else:
            return orders
