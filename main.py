from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to my server"


@app.get("/products")
def get_products():
    return products


##Path parameter: fixed set of parameters can be passed in the url, and we can access those parameters in the function.
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    #if product available with the id, return product, lese return error mesage.

    for oneProduct in products:
        if oneProduct.get("id")==product_id:
            return oneProduct
    

    return {"error":"product not found"}


##Query parameter: n number of parameters can be passed in the url, and we can access those parameters in the function.
@app.get("/greet")
def greet_user(request:Request):
    query_params= dict(request.query_params)
    print(query_params)
    if(int(query_params.get('age'))<18):
        return {"message": "Sorry you are not old enough to use this page"}

    return {"greet": f"Hello, welcome {query_params.get('name')} to my server, You are {query_params.get('age')} years old."}

    ## different types pf HTTP Mehods

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data=product_data.model_dump()
    products.append(product_data)
    return {"status":"Product created successfully", "data":products}
    
    
@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id:int):
    for index,oneProduct in enumerate(products):
       if(oneProduct.get("id")==product_id):
        products[index]=product_data.model_dump()
        return {"status": "Product updated succesfully!","product":product_data}


    return {"error":"product not found"}

# Delete product function
@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,oneProduct in enumerate(products):
        if(oneProduct.get("id")==product_id):
            deleted_product=products.pop(index)
            return {"status":"product deleted succesfully!!", "product":deleted_product}

    return {"status": f"Product with ID {product_id}doesn't exist!!"}

## How to call different HTTO Methods. -- Any TOOl?
## how to validate data. - DTOS(Data Transfer Objects) - Pydantic Models
## I will be completing authentication part by either 12-02-26 night or 13-05-26.


