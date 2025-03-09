import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from backend.users.router import router as router_user
from backend.Student.router import router as router_student
from backend.Status.router import router as router_status
from backend.Skill.router import router as router_skill
from backend.Vacancy.router import router as router_vacancy
from backend.Message.router import router as router_message
from backend.Organisation.router import router as router_organization
from backend.Employer.router import router as router_employer
from backend.Feedback.router import router as router_feedback
from backend.Interview.router import router as router_interview
from backend.Application.router import router as router_application


app = FastAPI()
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)

app.include_router(router_user)
app.include_router(router_student)
app.include_router(router_skill)
app.include_router(router_status)
app.include_router(router_vacancy)
app.include_router(router_message)
app.include_router(router_organization)
app.include_router(router_message)
app.include_router(router_employer)
app.include_router(router_feedback)
app.include_router(router_interview)
app.include_router(router_application)

@app.get("/")
async def root():
    return {"message": "Hello World"}



