import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.face_service import FaceRecognitionService
from app.services.registry import RegistryService

router = APIRouter(tags=["Face Registry"])

face_service = FaceRecognitionService()
registry_service = RegistryService()


@router.post("/register")
async def register_person(
    name: str = Form(...),
    image: UploadFile = File(...)
):
    try:
        os.makedirs("uploads", exist_ok=True)

        image_path = os.path.join("uploads", image.filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        embedding = face_service.get_embedding(image_path)

        person = registry_service.register_person(
            name=name,
            embedding=embedding,
            image_path=image_path
        )

        return {
            "message": "Person registered successfully",
            "person": {
                "id": person.id,
                "name": person.name,
                "image": person.image_path
            }
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
