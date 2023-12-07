from modules.Product.repositories.ProductRepository import ProductRepository


class FindAllProductsService():
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        projects = self.repository.find_all()

        return projects
