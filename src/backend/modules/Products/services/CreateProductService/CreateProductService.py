from modules.Product.models.Product import Product
from modules.Product.repositories.ProductRepository import ProductRepository

class ProductCustomerService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: Product):
        foundProduct = self.repository.find_by_name(email=product.email)

        if foundProduct is Product:
            return "Already exists an product with this name!"
        else:
            newProduct = self.repository.create(product=product)
            return newProduct
