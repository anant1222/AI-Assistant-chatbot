from fastapi import FastAPI
from config import settings
from routes import api, auth

app = FastAPI()

app.include_router(api.router, prefix="/api")
app.include_router(auth.router, prefix="/auth")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
