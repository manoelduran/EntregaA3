from fastapi import Depends
from modules.Product.repositories.ProductRepository import ProductRepository
from modules.Product.services.FindAllProductsService.FindAllProductsService import FindAllProductsService
from modules.Product.services.FindOneProductService.FindOneProductService import FindOneProductService
from infrastructure.database.sqliteDatabase import SqliteDatabase
from modules.Product.services.CreateProductService.CreateProductService import CreateProductService
from modules.Product.services.DeleteProductService.DeleteProductService import DeleteProductService
from modules.Product.services.UpdateProductService.UpdateProductService import UpdateProductService


def get_db():
    db = SqliteDatabase("store.db")
    db.connect()
    return db


def product_repository_injection(database: SqliteDatabase = Depends(get_db)):
    return ProductRepository(database)


def find_all_product_service_injection(repository: ProductRepository = Depends(product_repository_injection)):
    return FindAllProductsService(repository)


def find_one_product_service_injection(repository: ProductRepository = Depends(product_repository_injection)):
    return FindOneProductService(repository)


def create_product_service_injection(repository: ProductRepository = Depends(product_repository_injection)):
    return CreateProductService(repository)


def update_product_service_injection(repository: ProductRepository = Depends(product_repository_injection)):
    return UpdateProductService(repository)


def delete_product_service_injection(repository: ProductRepository = Depends(product_repository_injection)):
    return DeleteProductService(repository)
