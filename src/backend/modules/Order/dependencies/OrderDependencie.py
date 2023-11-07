from fastapi import Depends
from modules.Order.services.CreateOrderService.CreateOrderService import CreateOrderService
from modules.Order.services.DeleteOrderService.DeleteOrderService import DeleteOrderService
from modules.Order.services.FindAllOrdersService.FindAllOrdersService import FindAllOrdersService
from modules.Order.services.FindOneOrderService.FindOneOrderService import FindOneOrderService
from modules.Order.services.UpdateOrderService.UpdateOrderService import UpdateOrderService
from modules.Order.repositories.OrderRepository import OrderRepository
from infrastructure.database.sqliteDatabase import SqliteDatabase


def get_db():
    db = SqliteDatabase("store.db")
    db.connect()
    return db


def order_repository_injection(database: SqliteDatabase = Depends(get_db)):
    return OrderRepository(database)


def find_all_order_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return FindAllOrdersService(repository)


def find_one_order_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return FindOneOrderService(repository)


def create_order_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return CreateOrderService(repository)


def update_order_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return UpdateOrderService(repository)


def delete_order_service_injection(repository: OrderRepository = Depends(order_repository_injection)):
    return DeleteOrderService(repository)
