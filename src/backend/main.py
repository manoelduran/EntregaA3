from fastapi import FastAPI
from modules.Customer.routes.customer import customerRouter


class Main:
    app: FastAPI

    def __init__(self):
        self.app = FastAPI()

    def routes(self):
        self.app.include_router(customerRouter)
        self.app.include_router(customerRouter)
        self.app.include_router(customerRouter)

