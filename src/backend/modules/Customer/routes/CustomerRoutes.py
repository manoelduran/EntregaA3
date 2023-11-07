from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from modules.Customer.dtos.UpdateCustomerDto import UpdateCustomerDto
from modules.Customer.dtos.CreateCustomerDto import CreateCustomerDto
from modules.Customer.models.Customer import Customer
from modules.Customer.services.CreateCustomerService.CreateCustomerService import CreateCustomerService
from modules.Customer.services.UpdateCustomerService.UpdateCustomerService import UpdateCustomerService
from modules.Customer.services.DeleteCustomerService.DeleteCustomerService import DeleteCustomerService
from modules.Customer.services.FindAllCustomersService.FindAllCustomersService import FindAllCustomersService
from modules.Customer.services.FindOneCustomerService.FindOneCustomerService import FindOneCustomerService
from modules.Customer.dependencies.CustomerDependencie import create_customer_service_injection, find_all_customer_service_injection, find_one_customer_service_injection, update_customer_service_injection, delete_customer_service_injection

customerRouter = APIRouter(prefix="/customers", tags=["customers"])


@customerRouter.get("/", response_model=list[Customer], status_code=200)
def find_all(service: FindAllCustomersService = Depends(find_all_customer_service_injection)):
    return service.execute()


@customerRouter.get("/{id}", response_model=Union[Customer, str], status_code=200)
def find_one(id: int, service: FindOneCustomerService = Depends(find_one_customer_service_injection)):
    foundCustomer = service.execute(id)
    if isinstance(foundCustomer, Customer):
        return foundCustomer.json()
    else:
        raise HTTPException(
            status_code=404, detail="Customer not found!")


@customerRouter.post("/", response_model=Union[CreateCustomerDto, str], status_code=201)
def create(customer: CreateCustomerDto, service: CreateCustomerService = Depends(create_customer_service_injection)):
    newCustomer = service.execute(customer)
    if isinstance(newCustomer, CreateCustomerDto):
        return newCustomer
    else:
        raise HTTPException(
            status_code=400, detail="Already exists an customer with this email!")


@customerRouter.put("/{id}", response_model=Union[UpdateCustomerDto, str], status_code=200)
def update(id: int, customer: UpdateCustomerDto,  service: UpdateCustomerService = Depends(update_customer_service_injection)):
    foundCustomer = service.execute(id, customer)
    if isinstance(foundCustomer, UpdateCustomerDto):
        return foundCustomer
    else:
        raise HTTPException(
            status_code=404, detail="Customer not found!")


@customerRouter.delete("/{id}", response_model=Union[Customer, str])
def delete(id: int, service: DeleteCustomerService = Depends(delete_customer_service_injection)):
    foundCustomer = service.execute(id)
    if isinstance(foundCustomer, Customer):
        return JSONResponse(status_code=204, content=foundCustomer.json())
    else:
        raise HTTPException(
            status_code=404, detail="Customer not found!")
