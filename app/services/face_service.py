import cv2
import numpy as np
from insightface.app import FaceAnalysis


class FaceRecognitionService:

    def __init__(self):
        self.app = FaceAnalysis(
            providers=["CPUExecutionProvider"]
        )
        self.app.prepare(ctx_id=0)

    def get_embedding(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise Exception(f"Cannot read image: {image_path}")

        faces = self.app.get(image)

        if len(faces) == 0:
            raise Exception("No face detected")

        if len(faces) > 1:
            raise Exception("Multiple faces detected")

        embedding = faces[0].embedding

        print("Embedding Shape:", faces[0].embedding.shape)
        print("Embedding Type:", type(faces[0].embedding))
        print("First 20 Values:")
        print(faces[0].embedding[:20])

        return faces[0].embedding

    def compare_faces(self, image1, image2):

        emb1 = self.get_embedding(image1)
        emb2 = self.get_embedding(image2)

    # Normalize embeddings
        emb1 = emb1 / np.linalg.norm(emb1)
        emb2 = emb2 / np.linalg.norm(emb2)

    # Cosine similarity
        similarity = np.dot(emb1, emb2)

        return float(similarity)
