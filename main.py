from fastapi import FastAPI
from core.config import get_settings
from api.v1.router import api_router

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI AI Project"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
