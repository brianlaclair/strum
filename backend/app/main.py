from fastapi import FastAPI

app = FastAPI(title="Strum API")

@app.get("/")
async def root():
    return {"message": "Hello World"}

