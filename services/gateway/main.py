from fastapi import FastAPI
import requests

app = FastAPI(title="KubeCommerce API Gateway")


PRODUCTS_SERVICE = "http://products:8000"
ORDERS_SERVICE = "http://orders:8000"
USERS_SERVICE = "http://users:8000"


@app.get("/")
def root():
    return {
        "service": "api-gateway",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products")
def get_products():
    response = requests.get(f"{PRODUCTS_SERVICE}/products")
    return response.json()


@app.get("/orders")
def get_orders():
    response = requests.get(f"{ORDERS_SERVICE}/orders")
    return response.json()


@app.get("/users")
def get_users():
    response = requests.get(f"{USERS_SERVICE}/users")
    return response.json()
