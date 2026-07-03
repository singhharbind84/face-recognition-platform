from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.face_service import FaceRecognitionService

router = APIRouter()

service = FaceRecognitionService()


@router.post("/verify")
async def verify(
    image1: UploadFile = File(...),
    image2: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    path1 = f"uploads/{image1.filename}"
    path2 = f"uploads/{image2.filename}"

    with open(path1, "wb") as buffer:
        shutil.copyfileobj(image1.file, buffer)

    with open(path2, "wb") as buffer:
        shutil.copyfileobj(image2.file, buffer)

    score = service.compare_faces(path1, path2)

    return {
        "match": score > 0.7,
        "similarity": score
    }
