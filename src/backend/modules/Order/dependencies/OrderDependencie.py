from fastapi import Depends
from modules.Order.services.CreateOrderService.CreateOrderService import CreateOrderService
from modules.Order.services.DeleteOrderService.DeleteOrderService import DeleteOrderService
from modules.Order.services.FindAllOrdersService.FindAllOrdersService import FindAllOrdersService
from modules.Order.services.FindOneOrderService.FindOneOrderService import FindOneOrderService
from modules.Order.services.UpdateOrderService.UpdateOrderService import UpdateOrderService
from modules.Order.services.FindAllOrdersByCustomerIdService.FindAllOrdersByCustomerIdService import FindAllOrdersByCustomerIdService
from modules.Order.services.FindAllOrdersByProductIdService.FindAllOrdersByProductIdService import FindAllOrdersByProductIdService
from modules.Order.repositories.OrderRepository import OrderRepository
from modules.Product.repositories.ProductRepository import ProductRepository
from modules.Product.dependencies.ProductDependencie import product_repository_injection
from modules.Customer.dependencies.CustomerDependencie import customer_repository_injection
from modules.Customer.repositories.CustomerRepository import CustomerRepository
from infrastructure.database.sqliteDatabase import SqliteDatabase


def get_db():
    db = SqliteDatabase("store.db")
    db.connect()
    return db


def order_repository_injection(database: SqliteDatabase = Depends(get_db)):
    return OrderRepository(database)


def find_all_order_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return FindAllOrdersService(repository)


def find_all_order_by_customerId_service_injection(repository: OrderRepository = Depends(order_repository_injection), product_repository: ProductRepository = Depends(product_repository_injection)):
    return FindAllOrdersByCustomerIdService(repository, product_repository)


def find_all_order_by_productId_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return FindAllOrdersByProductIdService(repository)


def find_one_order_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return FindOneOrderService(repository)


def create_order_service_injection(repository: OrderRepository = Depends(order_repository_injection), product_repository: ProductRepository = Depends(product_repository_injection), customer_repository: CustomerRepository = Depends(customer_repository_injection)):
    return CreateOrderService(repository, product_repository, customer_repository)


def update_order_service_injection(repository: OrderRepository = Depends(order_repository_injection), product_repository: ProductRepository = Depends(product_repository_injection), customer_repository: CustomerRepository = Depends(customer_repository_injection)):
    return UpdateOrderService(repository, product_repository, customer_repository)


def delete_order_service_injection(repository: OrderRepository = Depends(order_repository_injection), product_repository: ProductRepository = Depends(product_repository_injection),):
    return DeleteOrderService(repository, product_repository)
