from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from backend.Employer.rb import RBEmployer
from backend.Employer.router import get_all_employers
from backend.Student.rb import RBStudent
from backend.Student.router import get_student_by_id, get_all_students
from backend.users.router import get_me
router = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='frontend/templates')


@router.get('/')
async def get_home(request: Request):
    return templates.TemplateResponse(name='home.html', context={'request': request})


@router.get('/register')
async def get_register_html(request: Request):
    return templates.TemplateResponse(name='register_form.html', context={'request': request})


@router.get('/login')
async def get_login_html(request: Request):
    return templates.TemplateResponse(name='login_form.html', context={'request': request})


@router.get('/profile')
async def get_my_profile(request: Request, profile=Depends(get_me)):
    if profile.student_id is not None:
        student = await get_student_by_id(profile.student_id)
        return templates.TemplateResponse(name='profile.html', context={'request': request, 'role': 1, 'student': student, 'profile': profile})
    if profile.employer_id is not None:
        employer = await get_all_employers(RBEmployer(id=profile.employer_id))
        return templates.TemplateResponse(name='profile.html', context={'request': request,'role': 2, 'employer': employer, 'profile': profile})
    return templates.TemplateResponse(name='profile.html', context={'request': request, 'role': 0})


@router.get('/create_student')
async def get_register_html(request: Request):
    return templates.TemplateResponse(name='createStudent.html', context={'request': request})