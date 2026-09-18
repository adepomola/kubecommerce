from fastapi import FastAPI

app = FastAPI(title="KubeCommerce Orders Service")


@app.get("/")
def root():
    return {"service": "orders", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/orders")
def get_orders():
    return [
        {"id": 1, "product": "Laptop", "quantity": 1, "status": "confirmed"},
        {"id": 2, "product": "Wireless Mouse", "quantity": 2, "status": "processing"},
        {"id": 3, "product": "Mechanical Keyboard", "quantity": 1, "status": "shipped"},
    ]
