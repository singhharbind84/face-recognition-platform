from fastapi import FastAPI

from app.routes.verify import router as verify_router
from app.routes.register import router as register_router

from app.routes.persons import router as persons_router


app = FastAPI(
    title="Face Recognition API",
    version="1.0.0"
)

app.include_router(verify_router)
app.include_router(register_router)
app.include_router(persons_router)

@app.get("/")
def health():
    return {
        "status": "running"
    }
