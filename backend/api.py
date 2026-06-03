from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from workflow import user_proxy, manager

import os
import glob

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic: str


@app.get("/")
def home():
    return {
        "message": "Multi-Agent Research Assistant API Running"
    }


@app.post("/research")
def research(request: ResearchRequest):

    try:

        # Run AutoGen workflow
        user_proxy.initiate_chat(
            manager,
            message=request.topic
        )

        # Find newest generated report
        reports = glob.glob("reports/*.md")

        if not reports:
            return {
                "status": "error",
                "message": "No report generated"
            }

        latest_report = max(
            reports,
            key=os.path.getctime
        )

        # Read report contents
        with open(latest_report, "r", encoding="utf-8") as f:
            final_report = f.read()

        return {
            "status": "success",
            "topic": request.topic,
            "report": final_report
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }