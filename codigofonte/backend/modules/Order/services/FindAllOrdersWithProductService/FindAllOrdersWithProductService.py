from modules.Order.dtos.FindAllByCustomerDto import FindAllByCustomerDto
from typing import List
from modules.Product.repositories.ProductRepository import ProductRepository
from modules.Order.repositories.OrderRepository import OrderRepository


class FindAllOrdersWithProductService():
    def __init__(self, repository: OrderRepository, product_repository: ProductRepository):
        self.repository = repository
        self.product_repository = product_repository

    def execute(self):
        formatted_orders: List[FindAllByCustomerDto] = []
        orders = self.repository.find_all_with_project()
        if orders is None:

            return "Orders not found!"
        else:
            for order in orders:
                product = self.product_repository.find_one(order.product_id)
                formatted_order = FindAllByCustomerDto(
                    id=order.id,
                    customer_id=order.customer_id,
                    product_id=order.product_id,
                    quantity=order.quantity,
                    product_name=product.name,
                    price=product.price,
                    ordered_at=order.ordered_at
                )
                formatted_orders.append(formatted_order)
            return formatted_orders
