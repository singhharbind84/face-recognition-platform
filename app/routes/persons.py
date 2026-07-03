from fastapi import APIRouter

from app.services.registry import RegistryService

router = APIRouter(tags=["Persons"])

registry_service = RegistryService()


@router.get("/persons")
def list_persons():

    persons = registry_service.list_persons()

    return [
        {
            "id": person.id,
            "name": person.name,
            "image": person.image_path
        }
        for person in persons
    ]
