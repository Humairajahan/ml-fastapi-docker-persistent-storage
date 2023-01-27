from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.model.model import predict_pipeline

app = FastAPI(title="dockerizing ml model with persistent storage")

app.add_middleware( CORSMiddleware,
                    allow_credentials=True,
                    allow_origins=["*"],
                    allow_methods=["*"],
                    allow_headers=["*"] )


@app.get("/")
def home_page():
    return "dockerizing ml model with persistent storage!"


@app.post("/model-prediction")
async def model_prediction(text: str):
    output = predict_pipeline(text)
    return {"language": output}