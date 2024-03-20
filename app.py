from summarize import Summarizer
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Summer Internship",
    description="A simple API to summarize text",
    version="0.1.0",  
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/", response_class=PlainTextResponse, tags=["Home"])
async def home():
    return "Welcome to the home page"

@app.post("/summarize", tags=["Summarize"])
async def summarize(text: str):
    summarizer = Summarizer()
    summary = summarizer.get_summary(text)
    return summary




