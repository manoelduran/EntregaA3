from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from modules.Order.services.CreateOrderService.CreateOrderService import CreateOrderService
from modules.Order.services.DeleteOrderService.DeleteOrderService import DeleteOrderService
from modules.Order.services.FindAllOrdersService.FindAllOrdersService import FindAllOrdersService
from modules.Order.services.FindOneOrderService.FindOneOrderService import FindOneOrderService
from modules.Order.services.UpdateOrderService.UpdateOrderService import UpdateOrderService
from modules.Order.dtos.UpdateOrderDto import UpdateOrderDto
from modules.Order.dtos.CreateOrderDto import CreateOrderDto
from modules.Order.models.Order import Order
from modules.Order.dependencies.OrderDependencie import find_all_order_service_injection, find_one_order_service_injection, create_order_service_injection, update_order_service_injection, delete_order_service_injection

orderRouter = APIRouter(prefix="/orders", tags=["orders"])


@orderRouter.get("/", response_model=list[Order], status_code=200)
def find_all(service: FindAllOrdersService = Depends(find_all_order_service_injection)):
    return service.execute()


@orderRouter.get("/{id}", response_model=Union[Order, str], status_code=200)
def find_one(id: int, service: FindOneOrderService = Depends(find_one_order_service_injection)):
    foundOrder = service.execute(id)
    if isinstance(foundOrder, Order):
        return foundOrder.json()
    else:
        raise HTTPException(
            status_code=404, detail="Order not found!")


@orderRouter.post("/", response_model=Union[CreateOrderDto, str], status_code=201)
def create(order: CreateOrderDto, service: CreateOrderService = Depends(create_order_service_injection)):
    newOrder = service.execute(order)
    if isinstance(newOrder, CreateOrderDto):
        return newOrder
    else:
        raise HTTPException(
            status_code=400, detail="Already exists an order with this email!")


@orderRouter.put("/{id}", response_model=Union[UpdateOrderDto, str], status_code=200)
def update(id: int, order: UpdateOrderDto,  service: UpdateOrderService = Depends(update_order_service_injection)):
    foundOrder = service.execute(id, order)
    if isinstance(foundOrder, UpdateOrderDto):
        return foundOrder
    else:
        raise HTTPException(
            status_code=404, detail="Order not found!")


@orderRouter.delete("/{id}", response_model=Union[Order, str])
def delete(id: int, service: DeleteOrderService = Depends(delete_order_service_injection)):
    foundOrder = service.execute(id)
    if isinstance(foundOrder, Order):
        return JSONResponse(status_code=204, content=foundOrder.json())
    else:
        raise HTTPException(
            status_code=404, detail="Order not found!")
