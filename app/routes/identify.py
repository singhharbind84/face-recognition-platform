import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.face_service import FaceRecognitionService
from app.services.registry import RegistryService

router = APIRouter(tags=["Face Identification"])

face_service = FaceRecognitionService()
registry_service = RegistryService()


@router.post("/identify")
async def identify(image: UploadFile = File(...)):
    try:

        os.makedirs("uploads", exist_ok=True)

        image_path = os.path.join("uploads", image.filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        embedding = face_service.get_embedding(image_path)

        result = registry_service.identify_person(embedding)

        if result is None:
            return {
                "match": False,
                "person": None,
                "similarity": 0
            }

        person = result["person"]
        score = result["score"]

        threshold = 0.50

        if score >= threshold:
            return {
                "match": True,
                "similarity": round(score, 4),
                "person": {
                    "id": person.id,
                    "name": person.name,
                    "image": person.image_path
                }
            }

        return {
            "match": False,
            "similarity": round(score, 4),
            "person": None
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
