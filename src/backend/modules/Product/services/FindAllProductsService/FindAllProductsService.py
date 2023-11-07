from modules.Product.repositories.ProductRepository import ProductRepository


class FindAllProductsService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        ola = self.repository.find_all()
        print("ola", ola)
        return ola
