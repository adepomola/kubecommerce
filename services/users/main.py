from fastapi import FastAPI

app = FastAPI(title="KubeCommerce Users Service")


@app.get("/")
def root():
    return {"service": "users", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
        {"id": 3, "name": "Alex Johnson", "email": "alex@example.com"},
    ]
