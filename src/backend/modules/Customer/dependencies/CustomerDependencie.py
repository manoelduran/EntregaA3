from fastapi import Depends
from modules.Customer.repositories.CustomerRepository import CustomerRepository
from modules.Customer.services.FindAllCustomersService.FindAllCustomersService import FindAllCustomersService
from modules.Customer.services.FindOneCustomerService.FindOneCustomerService import FindOneCustomerService
from infrastructure.database.sqliteDatabase import SqliteDatabase


def get_db():
    db = SqliteDatabase("store.db")
    return db


def customer_repository_injection(database: SqliteDatabase = Depends(get_db)):
    return CustomerRepository(database)


def find_all_customer_service_injection(repository: CustomerRepository = Depends(customer_repository_injection)):
    return FindAllCustomersService(repository)


def find_one_customer_service_injection(repository: CustomerRepository = Depends(customer_repository_injection)):
    return FindOneCustomerService(repository)
