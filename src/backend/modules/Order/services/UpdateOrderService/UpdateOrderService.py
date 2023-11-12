from modules.Order.dtos.UpdateOrderDto import UpdateOrderDto
from modules.Order.repositories.OrderRepository import OrderRepository
from modules.Product.repositories.ProductRepository import ProductRepository
from modules.Customer.repositories.CustomerRepository import CustomerRepository


class UpdateOrderService():
    def __init__(self, repository: OrderRepository, product_repository: ProductRepository, customer_repository: CustomerRepository):
        self.repository = repository
        self.product_repository = product_repository
        self.customer_repository = customer_repository

    def execute(self, id: int, order: UpdateOrderDto):
        foundOrder = self.repository.find_one(
            id=id)
        if foundOrder is None:
            return "Order not found!"
        foundCustomer = self.customer_repository.find_one(
            id=order.customer_id)
        if foundCustomer is None:
            return "You only can update an order that you ordered! Your customer_id doesn't match with the current customer_id from this order."
        foundProduct = self.product_repository.find_one(
            id=order.product_id)
        if foundProduct is None:
            return "This product are out of stock!"
        if order.quantity != foundOrder.quantity:
            if order.quantity > foundOrder.quantity:
                print("order 1", order)
                print("foundOrder 1", foundOrder)
                foundProduct.quantity = foundProduct.quantity - \
                    (order.quantity - foundOrder.quantity)
                print("foundProduct ATUALIZADO 1", foundProduct)
                updatedProduct = self.product_repository.update(
                    order.product_id, product=foundProduct)
                print("updatedProduct 1", updatedProduct)
                updatedOrder = self.repository.update(id, order=order)
                return updatedOrder
            else:
                print("order 2", order)
                print("foundOrder 2", foundOrder)
                foundProduct.quantity = foundProduct.quantity + \
                    (foundOrder.quantity - order.quantity)
                print("foundProduct ATUALIZADO 2", foundProduct)
                updatedProduct = self.product_repository.update(
                    order.product_id, product=foundProduct)
                print("updatedProduct 2", updatedProduct)
                updatedOrder = self.product_repository.update(
                    order.product_id, product=foundProduct)
                updatedOrder = self.repository.update(id, order=order)
                return updatedOrder
