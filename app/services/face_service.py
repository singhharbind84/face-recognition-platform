import cv2
import numpy as np

from app.core.model import face_app


class FaceRecognitionService:

    def get_embedding(self, image_path: str) -> np.ndarray:
        """
        Extract a 512-dimensional face embedding from an image.
        """

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(f"Unable to read image: {image_path}")

        faces = face_app.get(image)

        if len(faces) == 0:
            raise ValueError("No face detected in the image.")

        if len(faces) > 1:
            raise ValueError(
                "Multiple faces detected. Please upload an image containing only one face."
            )

        embedding = faces[0].embedding

        return embedding

    def compare_faces(self, image1: str, image2: str) -> float:
        """
        Compare two faces using cosine similarity.
        Returns a similarity score between -1 and 1.
        """

        emb1 = self.get_embedding(image1)
        emb2 = self.get_embedding(image2)

        # Normalize embeddings
        emb1 = emb1 / np.linalg.norm(emb1)
        emb2 = emb2 / np.linalg.norm(emb2)

        similarity = np.dot(emb1, emb2)

        return float(similarity)

    def get_face_info(self, image_path: str) -> dict:
        """
        Return useful metadata about a detected face.
        """

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(f"Unable to read image: {image_path}")

        faces = face_app.get(image)

        if len(faces) == 0:
            raise ValueError("No face detected.")

        if len(faces) > 1:
            raise ValueError("Multiple faces detected.")

        face = faces[0]

        return {
            "bbox": face.bbox.tolist(),
            "age": int(face.age),
            "gender": "Male" if face.gender == 1 else "Female",
            "det_score": float(face.det_score),
            "embedding": face.embedding.tolist()
        }
