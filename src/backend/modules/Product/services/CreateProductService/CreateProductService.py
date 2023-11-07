from modules.Product.dtos.CreateProductDto import CreateProductDto
from modules.Product.models.Product import Product
from modules.Product.repositories.ProductRepository import ProductRepository


class CreateProductService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: CreateProductDto):
        foundProduct = self.repository.find_by_name(name=product.name)

        if foundProduct is Product:
            return "Already exists an product with this id!"
        else:
            newProduct = self.repository.create(product=product)
            return newProduct
