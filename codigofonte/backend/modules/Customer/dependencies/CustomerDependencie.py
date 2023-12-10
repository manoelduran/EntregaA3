from fastapi import Depends
from modules.Customer.repositories.CustomerRepository import CustomerRepository
from modules.Customer.services.FindAllCustomersService.FindAllCustomersService import FindAllCustomersService
from modules.Customer.services.FindOneCustomerService.FindOneCustomerService import FindOneCustomerService
from infrastructure.database.sqliteDatabase import SqliteDatabase
from modules.Customer.services.CreateCustomerService.CreateCustomerService import CreateCustomerService
from modules.Customer.services.DeleteCustomerService.DeleteCustomerService import DeleteCustomerService
from modules.Customer.services.UpdateCustomerService.UpdateCustomerService import UpdateCustomerService


def get_db():
    db = SqliteDatabase("store.db")
    db.connect()
    return db


def customer_repository_injection(database: SqliteDatabase = Depends(get_db)):
    return CustomerRepository(database)


def find_all_customer_service_injection(repository: CustomerRepository = Depends(customer_repository_injection)):
    return FindAllCustomersService(repository)


def find_one_customer_service_injection(repository: CustomerRepository = Depends(customer_repository_injection)):
    return FindOneCustomerService(repository)


def create_customer_service_injection(repository: CustomerRepository = Depends(customer_repository_injection)):
    return CreateCustomerService(repository)


def update_customer_service_injection(repository: CustomerRepository = Depends(customer_repository_injection)):
    return UpdateCustomerService(repository)


def delete_customer_service_injection(repository: CustomerRepository = Depends(customer_repository_injection)):
    return DeleteCustomerService(repository)
