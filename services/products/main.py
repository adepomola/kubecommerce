from fastapi import FastAPI

app = FastAPI(title="KubeCommerce Products Service")


@app.get("/")
def root():
    return {"service": "products", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 850.00},
        {"id": 2, "name": "Wireless Mouse", "price": 25.00},
        {"id": 3, "name": "Mechanical Keyboard", "price": 75.00},
    ]
