from app.models.person import Person


class RegistryStore:

    def __init__(self):
        self._persons = []
        self._next_id = 1

    def add(self, name, embedding, image_path):

        person = Person(
            id=self._next_id,
            name=name,
            embedding=embedding,
            image_path=image_path
        )

        self._persons.append(person)
        self._next_id += 1

        return person

    def list(self):
        return self._persons

    def get(self, person_id):

        for person in self._persons:
            if person.id == person_id:
                return person

        return None

    def delete(self, person_id):

        person = self.get(person_id)

        if person:
            self._persons.remove(person)
            return True

        return False


registry_store = RegistryStore()
