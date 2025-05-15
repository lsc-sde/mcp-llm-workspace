from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default_root():
    return {"message": "FastAPI is working."}