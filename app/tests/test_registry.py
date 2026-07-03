import numpy as np

from app.services.registry import RegistryService

service = RegistryService()

person1 = service.register_person(
    "Harbind",
    np.random.rand(512),
    "uploads/person1.jpg"
)

person2 = service.register_person(
    "Rahul",
    np.random.rand(512),
    "uploads/person2.jpg"
)

print("Registered Persons")
print("------------------")

for person in service.list_persons():
    print(person)

print()

print("Deleting Person 1")
service.delete_person(1)

print()

print("Remaining Persons")

for person in service.list_persons():
    print(person)
