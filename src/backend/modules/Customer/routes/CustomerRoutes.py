from fastapi import APIRouter, Depends
from modules.Customer.models.Customer import Customer
from modules.Customer.services.FindAllCustomersService.FindAllCustomersService import FindAllCustomersService
from modules.Customer.dependencies.CustomerDependencie import find_all_customer_service_injection, find_one_customer_service_injection

customerRouter = APIRouter(prefix="/customers", tags=["customers"])


@customerRouter.get("/", response_model=list[Customer])
def find_all(service: FindAllCustomersService = Depends(find_all_customer_service_injection)):
    return service.execute()

@customerRouter.get("/{id}", response_model=Customer)
def find_one(service: FindAllCustomersService = Depends(find_one_customer_service_injection)):
    return service.execute()
