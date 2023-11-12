from modules.Order.dtos.CreateOrderDto import CreateOrderDto
from modules.Order.repositories.OrderRepository import OrderRepository
from modules.Product.repositories.ProductRepository import ProductRepository
from modules.Customer.repositories.CustomerRepository import CustomerRepository


class CreateOrderService():
    def __init__(self, repository: OrderRepository, product_repository: ProductRepository, customer_repository: CustomerRepository):
        self.repository = repository
        self.product_repository = product_repository
        self.customer_repository = customer_repository

    def execute(self, order: CreateOrderDto):
        foundCustomer = self.customer_repository.find_one(
            id=order.customer_id)
        if foundCustomer is None:
            return "Does not exist a user with this customer_id!"
        foundProduct = self.product_repository.find_one(
            id=order.product_id)
        if foundProduct is None:
            return "This product are out of stock!"
        if order.quantity > foundProduct.quantity:
            return f"You can't buy more than the max stock of a product! {foundProduct.quantity}"
        else:
            foundProduct.quantity -= order.quantity
            self.product_repository.update(
                order.product_id, product=foundProduct)
            newOrder = self.repository.create(order=order)
            return newOrder
