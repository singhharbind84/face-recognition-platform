import cv2
from insightface.app import FaceAnalysis

# Load InsightFace
app = FaceAnalysis(providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)

# Read image
image = cv2.imread("images/person1.jpg")

if image is None:
    raise Exception("Image not found!")

# Detect faces
faces = app.get(image)

print(f"Faces detected: {len(faces)}")

for i, face in enumerate(faces):
    print("=" * 50)
    print(f"Face {i+1}")

    print("Bounding Box:", face.bbox)
    print("Detection Score:", face.det_score)
    print("Gender:", face.gender)
    print("Age:", face.age)

    print("Embedding Shape:", face.embedding.shape)
