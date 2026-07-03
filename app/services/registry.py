from app.storage.registry import registry_store


class RegistryService:

    def register_person(self, name, embedding, image_path):
        return registry_store.add(name, embedding, image_path)

    def list_persons(self):
        return registry_store.list()

    def get_person(self, person_id):
        return registry_store.get(person_id)

    def delete_person(self, person_id):
        return registry_store.delete(person_id)
