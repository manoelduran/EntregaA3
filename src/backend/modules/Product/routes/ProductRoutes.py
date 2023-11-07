from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from modules.Product.dtos.UpdateProductDto import UpdateProductDto
from modules.Product.dtos.CreateProductDto import CreateProductDto
from modules.Product.models.Product import Product
from modules.Product.services.CreateProductService.CreateProductService import CreateProductService
from modules.Product.services.UpdateProductService.UpdateProductService import UpdateProductService
from modules.Product.services.DeleteProductService.DeleteProductService import DeleteProductService
from modules.Product.services.FindAllProductsService.FindAllProductsService import FindAllProductsService
from modules.Product.services.FindOneProductService.FindOneProductService import FindOneProductService
from modules.Product.dependencies.ProductDependencie import create_product_service_injection, find_all_product_service_injection, find_one_product_service_injection, update_product_service_injection, delete_product_service_injection

ProductRoutes = APIRouter(prefix="/products", tags=["products"])


@ProductRoutes.get("/", response_model=list[Product], status_code=200)
def find_all(service: FindAllProductsService = Depends(find_all_product_service_injection)):
    return service.execute()


@ProductRoutes.get("/{id}", response_model=Union[Product, str], status_code=200)
def find_one(id: int, service: FindOneProductService = Depends(find_one_product_service_injection)):
    foundProduct = service.execute(id)
    if isinstance(foundProduct, Product):
        return foundProduct.json()
    else:
        raise HTTPException(
            status_code=404, detail="Product not found!")


@ProductRoutes.post("/", response_model=Union[CreateProductDto, str], status_code=201)
def create(product: CreateProductDto, service: CreateProductService = Depends(create_product_service_injection)):
    newProduct = service.execute(product)
    if isinstance(newProduct, CreateProductDto):
        return newProduct
    else:
        raise HTTPException(
            status_code=400, detail="Already exists an Product with this name!")


@ProductRoutes.put("/{id}", response_model=Union[UpdateProductDto, str], status_code=200)
def update(id: int, product: UpdateProductDto,  service: UpdateProductService = Depends(update_product_service_injection)):
    foundProduct = service.execute(id, product)
    if isinstance(foundProduct, UpdateProductDto):
        return foundProduct
    else:
        raise HTTPException(
            status_code=404, detail="Product not found!")


@ProductRoutes.delete("/{id}", response_model=Union[Product, str])
def delete(id: int, service: DeleteProductService = Depends(delete_product_service_injection)):
    foundProduct = service.execute(id)
    if isinstance(foundProduct, Product):
        return JSONResponse(status_code=204, content=foundProduct.json())
    else:
        raise HTTPException(
            status_code=404, detail="Product not found!")
