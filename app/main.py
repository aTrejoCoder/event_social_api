from fastapi import FastAPI
from .routers.router import router

app = FastAPI()

app.include_router(router, prefix="/v1/api", tags=["users"])
app.include_router(router, prefix="/v1/api", tags=["events"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)