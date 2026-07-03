from insightface.app import FaceAnalysis

print("Loading InsightFace model...")

face_app = FaceAnalysis(
    providers=["CPUExecutionProvider"]
)

face_app.prepare(ctx_id=0)

print("InsightFace model loaded successfully.")
