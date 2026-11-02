from fastapi import FastAPI

app = FastAPI(
    title="RaktSetu API",
    description="Smart Blood Request Coordination Platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to RaktSetu API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "raktsetu-api"
    }
    