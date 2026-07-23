from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.analyze import router

app = FastAPI(title="ResumeIQ API")

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://resumeiq-f.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "ResumeIQ API Running 🚀"}
