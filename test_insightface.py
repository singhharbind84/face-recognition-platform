from insightface.app import FaceAnalysis

print("Loading model...")

app = FaceAnalysis(
    providers=["CPUExecutionProvider"]
)

app.prepare(ctx_id=0)

print("Model loaded successfully!")
