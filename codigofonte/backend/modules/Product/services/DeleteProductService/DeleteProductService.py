from modules.Product.repositories.ProductRepository import ProductRepository


class DeleteProductService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, id: int):
        product = self.repository.find_one(id)

        if product is None:
            return "Product not found!"
        else:
            self.repository.delete(id)