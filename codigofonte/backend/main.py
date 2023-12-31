from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.Product.routes.ProductRoutes import product_router
from infrastructure.database.schema import tables_schema
from infrastructure.database.sqliteDatabase import SqliteDatabase
from modules.Customer.routes.CustomerRoutes import customer_router
from modules.Order.routes.OrderRoutes import order_router
from uvicorn import run


def get_db():
    db = SqliteDatabase("store.db")
    db.connect()
    db.create_tables(schema=tables_schema)
    db.seed_data()
    return db


app = FastAPI(title='API_ENTREGAA3')
origins = [
    "http://localhost:3000",
]

app.include_router(customer_router)
app.include_router(product_router)
app.include_router(order_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Server Running on port 8000!"}


if __name__ == "__main__":
    get_db()
    run("main:app", port=8000, reload=True)
