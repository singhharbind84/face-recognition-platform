from app.services.face_service import FaceRecognitionService

service = FaceRecognitionService()

score = service.compare_faces(
    "images/person1.jpg",
    "images/person2.jpg"
)

print("=" * 40)
print("Similarity Score:", score)

if score > 0.6:
    print("SAME PERSON")
else:
    print("DIFFERENT PERSON")
