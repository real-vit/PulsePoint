from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import crud_router
from inference_apis import inference_router

app = FastAPI()

origins = ["http://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud_router)
app.include_router(inference_router)

# uvicorn main:app --host 0.0.0.0 --port 3000
