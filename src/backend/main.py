from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.database.schema import tables_schema
from infrastructure.database.sqliteDatabase import SqliteDatabase
from modules.Customer.routes.CustomerRoutes import customerRouter
from uvicorn import run


def get_db():
    db = SqliteDatabase("store.db")
    db.connect()
    db.create_tables(schema=tables_schema)
    return db


app = FastAPI(title='API_ENTREGAA3')
origins = [
    "http://localhost:8000",
]

app.include_router(customerRouter)

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
