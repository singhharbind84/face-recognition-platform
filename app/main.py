from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes.verify import router as verify_router
from app.routes.register import router as register_router

from app.routes.persons import router as persons_router
from app.routes.identify import router as identify_router

app = FastAPI(
    title="Face Recognition API",
    version="1.0.0"
)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://192.168.75.168:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(verify_router)
app.include_router(register_router)
app.include_router(persons_router)
app.include_router(identify_router)

@app.get("/")
def health():
    return {
        "status": "running"
    }
