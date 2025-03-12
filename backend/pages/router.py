from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
import aiohttp
from backend.Employer.rb import RBEmployer
from backend.Employer.router import get_all_employers
from backend.Student.rb import RBStudent
from backend.Student.router import get_student_by_id, get_all_students
from backend.users.router import get_me


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

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
        student = await fetch(f'http://127.0.0.1:8000/api/students/?id={profile.student_id}')
        print(student)
        return templates.TemplateResponse(name='profile.html', context={'request': request, 'role': 1, 'student': student[0], 'profile': profile})
    if profile.employer_id is not None:
        employer = await fetch(f'http://127.0.0.1:8000/api/employers/?id={profile.employer_id}')
        print(employer)
        return templates.TemplateResponse(name='profile.html', context={'request': request,'role': 2, 'employer': employer[0], 'profile': profile})
    return templates.TemplateResponse(name='profile.html', context={'request': request, 'role': 0})


@router.get('/create_student')
async def get_create_student_html(request: Request):
    return templates.TemplateResponse(name='createStudent.html', context={'request': request})


@router.get('/create_employer')
async def get_create_employer_html(request: Request):
    return templates.TemplateResponse(name='createEmployer.html', context={'request': request})


@router.get('/vacancies')
async def get_vacancies_html(request: Request, user_data=Depends(get_me)):
    vacancies = await fetch(f'http://127.0.0.1:8000/api/vacancies/?id_employer={user_data.employer_id}')
    for vacancy in vacancies:
        levels = await fetch(f'http://127.0.0.1:8000/api/skills/')
        vacancy['level_skill'] = [level['level'] for level in levels if level['id'] == vacancy['level_skill']][0]
    return templates.TemplateResponse(name='vacancies.html', context={'request': request, 'vacancies': vacancies})


@router.get('/create_vacancy')
async def get_create_vacancy_html(request: Request, user_data=Depends(get_me)):
    return templates.TemplateResponse(name='createVacancy.html', context={'request': request, 'employer_id': user_data.employer_id})


@router.get('/find_vacancies')
async def get_find_vacancies_html(request: Request):
    vacancies =  await fetch(f'http://127.0.0.1:8000/api/vacancies')
    for vacancy in vacancies:
        levels = await fetch(f'http://127.0.0.1:8000/api/skills/')
        vacancy['level_skill'] = [level['level'] for level in levels if level['id'] == vacancy['level_skill']][0]
    return templates.TemplateResponse(name='findVacancy.html', context={'request': request, 'vacancies':vacancies})


@router.get('/my_applications')
async def get_create_vacancy_html(request: Request, user_data=Depends(get_me)):
    applications = await fetch(f'http://127.0.0.1:8000/api/applications/?id_student={user_data.student_id}')
    for application in applications:
        statuses = await fetch(f'http://127.0.0.1:8000/api/statuses/')
        application['status'], application['status_desc'] = [(status['name'], status['description']) for status in statuses if status['id'] == application['id_status']][0]
        vacancies = await fetch(f'http://127.0.0.1:8000/api/vacancies/?id={application["id_vacancy"]}')
        for vacancy in vacancies:
            if vacancy['id'] == application['id_vacancy']:
                application['post'], application['description'] = vacancy['post'], vacancy['description']
                employer = await fetch(f'http://127.0.0.1:8000/api/employers/?id={vacancy["id_employer"]}')
                employer = employer[0]
                application['employer_id'], application['employer_name'],  application['organization']= employer['id'], employer['name'], employer['organization']
                break
    return templates.TemplateResponse(name='myApplications.html', context={'request': request, 'applications': applications})