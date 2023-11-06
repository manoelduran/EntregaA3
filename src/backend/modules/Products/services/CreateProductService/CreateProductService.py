from modules.Product.models.Product import Product
from modules.Product.repositories.ProductRepository import ProductRepository

class ProductCustomerService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product: Product):
        foundProduct = self.repository.find_by_id(id=product.id)

        if foundProduct is Product:
            return "Already exists an product with this id!"
        else:
            newProduct = self.repository.create(product=product)
            return newProduct
