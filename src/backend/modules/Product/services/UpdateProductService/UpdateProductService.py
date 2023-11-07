from modules.Product.dtos.UpdateProductDto import UpdateProductDto
from modules.Product.repositories.ProductRepository import ProductRepository


class UpdateProductService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, id: int, product: UpdateProductDto):
        foundProduct = self.repository.find_one(id)

        if foundProduct is None:
            return "Product not found!"
        else:
            updatedProduct = self.repository.update(id, product)
            return updatedProduct
