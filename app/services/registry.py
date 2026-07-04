import numpy as np

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

    def identify_person(self, embedding):

        persons = self.list_persons()

        if len(persons) == 0:
            return None

        embedding = embedding / np.linalg.norm(embedding)

        best_person = None
        best_score = -1

        for person in persons:

            db_embedding = person.embedding
            db_embedding = db_embedding / np.linalg.norm(db_embedding)

            score = np.dot(embedding, db_embedding)

            if score > best_score:
                best_score = score
                best_person = person

        return {
            "person": best_person,
            "score": float(best_score)
        }
