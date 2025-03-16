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
        return templates.TemplateResponse(name='profile.html', context={'request': request, 'role': 1, 'student': student[0], 'profile': profile})
    if profile.employer_id is not None:
        employer = await fetch(f'http://127.0.0.1:8000/api/employers/?id={profile.employer_id}')
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
    levels = await fetch(f'http://127.0.0.1:8000/api/skills/')
    for vacancy in vacancies:
        vacancy['level_skill'] = [level['level'] for level in levels if level['id'] == vacancy['level_skill']][0]
    return templates.TemplateResponse(name='vacancies.html', context={'request': request, 'vacancies': vacancies})


@router.get('/vacancy')
async def get_vacancy_html(request: Request, id_vacancy, user_data=Depends(get_me)):
    vacancy = await fetch(f'http://127.0.0.1:8000/api/vacancies/?id={id_vacancy}')
    vacancy = vacancy[0]
    levels = await fetch(f'http://127.0.0.1:8000/api/skills/')
    vacancy['level_skill'] = [level['level'] for level in levels if level['id'] == vacancy['level_skill']][0]
    applications = await fetch(f'http://127.0.0.1:8000/api/applications/?id_vacancy={id_vacancy}')
    statuses = await fetch(f'http://127.0.0.1:8000/api/statuses/')
    for application in applications:
        student = await fetch(f'http://127.0.0.1:8000/api/students/?id={application["id_student"]}')
        student = student[0]
        interview = await fetch(f'http://127.0.0.1:8000/api/interviews/?id_student={application["id_student"]}&id_vacancy={id_vacancy}')
        if interview:
            interview = interview[0]
            application['interview'] = interview['id']
            application['interview_date'] = interview['date_start']
            application['interview_time'] = interview['time_start']
        else:
            application['interview'] = 0
            application['interview_date'] = 0
            application['interview_time'] = 0
        application['student'] = student['fio']
        application['speciality'] = student['speciality']
        application['course'] = student['course']
        application['ability'] = student['ability']
        application['level'] = [level['level'] for level in levels if level['id'] == student['level_skill']][0]
        application['status'] = [status['name'] for status in statuses if status['id'] == application['id_status']][0]
    return templates.TemplateResponse(name='vacancy.html', context={'request': request, 'vacancy': vacancy, 'applications': applications})

@router.get('/create_vacancy')
async def get_create_vacancy_html(request: Request, user_data=Depends(get_me)):
    return templates.TemplateResponse(name='createVacancy.html', context={'request': request, 'employer_id': user_data.employer_id})


@router.get('/find_vacancies')
async def get_find_vacancies_html(request: Request, ):
    vacancies =  await fetch(f'http://127.0.0.1:8000/api/vacancies/?is_active=true')
    levels = await fetch(f'http://127.0.0.1:8000/api/skills/')
    for vacancy in vacancies:
        vacancy['level_skill'] = [level['level'] for level in levels if level['id'] == vacancy['level_skill']][0]
    return templates.TemplateResponse(name='findVacancy.html', context={'request': request, 'vacancies':vacancies})


@router.get('/my_applications')
async def get_create_vacancy_html(request: Request, user_data=Depends(get_me)):
    applications = await fetch(f'http://127.0.0.1:8000/api/applications/?id_student={user_data.student_id}')
    for application in applications:
        print(application)
        statuses = await fetch(f'http://127.0.0.1:8000/api/statuses/')
        application['status'], application['status_desc'] = [(status['name'], status['description']) for status in statuses if status['id'] == application["id_status"]][0]
        vacancies = await fetch(f'http://127.0.0.1:8000/api/vacancies/?id={application["id_vacancy"]}')
        for vacancy in vacancies:
            if vacancy['id'] == application['id_vacancy']:
                application['post'], application['description'] = vacancy['post'], vacancy['description']
                employer = await fetch(f'http://127.0.0.1:8000/api/employers/?id={vacancy["id_employer"]}')
                employer = employer[0]
                application['employer_id'], application['employer_name'],  application['organization']= employer['id'], employer['name'], employer['organization']
                break
    return templates.TemplateResponse(name='myApplications.html', context={'request': request, 'applications': applications})


@router.get('/calendar')
async def get_calendar_html(request: Request, user_data=Depends(get_me)):
    interviews = await fetch(f'http://127.0.0.1:8000/api/interviews/ordered?id_student={user_data.student_id}')
    for interview in interviews:
        vacancy = await fetch(f'http://127.0.0.1:8000/api/vacancies/{interview["id_vacancy"]}')
        interview['post'] = vacancy['post']
        interview['salary'] = vacancy['salary']
        employer = await fetch(f'http://127.0.0.1:8000/api/employers/{vacancy["id_employer"]}')
        interview['organization'] = employer['organization']
    return templates.TemplateResponse(name='calendar.html', context={'request': request, 'interviews': interviews})


@router.get('/vacancy_profile')
async def get_vacancy_profile_html(request: Request, vacancy_id, user_data=Depends(get_me)):
    vacancy = await fetch(f'http://127.0.0.1:8000/api/vacancies/{vacancy_id}')
    levels = await fetch(f'http://127.0.0.1:8000/api/skills/')
    vacancy['level_skill'] = [level['level'] for level in levels if level['id'] == vacancy['level_skill']][0]
    employer = await fetch(f'http://127.0.0.1:8000/api/employers/{vacancy["id_employer"]}')
    vacancy['organization'] = employer['organization']
    vacancy['employer'] = employer['name']
    feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_to={vacancy["id"]}&path=1')
    for feedback in feedbacks:
        student = await fetch(f'http://127.0.0.1:8000/api/students/{feedback["id_from"]}')
        feedback['student'] = student['fio']
    return templates.TemplateResponse(name='profileVacancy.html', context={'request': request, 'vacancy': vacancy, 'feedbacks': feedbacks})


@router.get('/student_profile')
async def get_student_profile_html(request: Request, student_id):
    student = await fetch(f'http://127.0.0.1:8000/api/students/{student_id}')
    profile = await fetch(f'http://127.0.0.1:8000/api/auth/?student_id={student_id}')
    feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_to={student_id}&path=2')
    for feedback in feedbacks:
        employer = await fetch(f'http://127.0.0.1:8000/api/employers/{feedback["id_from"]}')
        feedback['employer'] = employer['name']
    return templates.TemplateResponse(name='profileStudent.html', context={'request': request, 'student': student, 'feedbacks': feedbacks, 'profile': profile[0]})


@router.get('/employer_profile')
async def get_student_profile_html(request: Request, employer_id):
    employer = await fetch(f'http://127.0.0.1:8000/api/employers/{employer_id}')
    profile = await fetch(f'http://127.0.0.1:8000/api/auth/?employer_id={employer_id}')
    feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_to={employer_id}&path=0')
    for feedback in feedbacks:
        student = await fetch(f'http://127.0.0.1:8000/api/students/{feedback["id_from"]}')
        feedback['student'] = student['fio']
    return templates.TemplateResponse(name='profileEmployer.html', context={'request': request, 'employer': employer, 'feedbacks': feedbacks, 'profile': profile[0]})


@router.get('/create_feedback')
async def get_create_feedback_html(request: Request, id_to, path, user_data=Depends(get_me)):
    can_post = False
    id_from = ''
    if user_data.student_id and (path == '1' or path == '0'):
        id_from = user_data.student_id
        can_post = True
    elif user_data.employer_id and (path == '2'):
        id_from = user_data.employer_id
        can_post = True
    return templates.TemplateResponse(name='createFeedback.html', context={'request': request, "id_to": id_to, 'id_from': id_from, 'path': path, 'can_post': can_post})


@router.get('/my_feedbacks')
async def get_my_feedbacks_html(request: Request, user_data=Depends(get_me)):
    type0 = []
    type1 = []
    type2 = []
    if user_data.student_id:
        feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_from={user_data.student_id}')
        for feedback in feedbacks:
            if feedback['path'] == 0:
                employer = await fetch(f'http://127.0.0.1:8000/api/employers/{feedback["id_to"]}')
                feedback['employer'] = employer['name']
                type0.append(feedback)
            elif feedback['path'] == 1:
                vacancy = await fetch(f'http://127.0.0.1:8000/api/vacancies/{feedback["id_to"]}')
                feedback['vacancy'] = vacancy['post']
                type1.append(feedback)
    else:
        feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_from={user_data.employer_id}&path=2')
        for feedback in feedbacks:
            student = await fetch(f'http://127.0.0.1:8000/api/students/{feedback["id_to"]}')
            feedback['student'] = student['fio']
            type2.append(feedback)
    return templates.TemplateResponse(name='myFeedback.html',
                                      context={'request': request, "type0": type0, "type1": type1, "type2": type2})


@router.get('/edit_feedback')
async def get_edit_feedback_html(request: Request, who, rate, desc, id_feedback):
    return templates.TemplateResponse(name='editFeedback.html',
                                      context={'request': request, "who": who, "rate": rate, "desc": desc, "id": id_feedback})


@router.get('/feedbacks_about_me')
async def get_feedbacks_about_me_html(request: Request, user_data=Depends(get_me)):
    if user_data.student_id:
        feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_to={user_data.student_id}&path=2')
        for feedback in feedbacks:
            employer = await fetch(f'http://127.0.0.1:8000/api/employers/{feedback["id_from"]}')
            feedback['who'] = employer['name']
    else:
        feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_to={user_data.employer_id}&path=0')
        for feedback in feedbacks:
            student = await fetch(f'http://127.0.0.1:8000/api/students/{feedback["id_from"]}')
            feedback['who'] = student['fio']
    return templates.TemplateResponse(name='feedbacksAboutMe.html',
                                      context={'request': request,})


@router.get('/edit_profile')
async def get_edit_profile_html(request: Request, user_data=Depends(get_me)):
    if user_data.student_id:
        student = await fetch(f'http://127.0.0.1:8000/api/students/{user_data.student_id}')
        return templates.TemplateResponse(name='editProfile.html',
                                          context={'request': request, 'role': 'student', 'student': student})
    else:
        employer = await fetch(f'http://127.0.0.1:8000/api/employers/{user_data.employer_id}')
        return templates.TemplateResponse(name='editProfile.html',
                                      context={'request': request,'employer': employer, 'role': 'employer'})


@router.get('/post_message')
async def get_post_message_html(request: Request, id_to, id_from, path, user_data=Depends(get_me)):
    if user_data.student_id:
        id_from = user_data.student_id
        vacancy = await fetch(f'http://127.0.0.1:8000/api/vacancies/{id_to}')
        return templates.TemplateResponse(name='createMessage.html',
                                          context={'request': request, 'id_to': id_to, 'path': path, 'id_from': id_from, 'vacancy': vacancy})
    else:
        student = await fetch(f'http://127.0.0.1:8000/api/students/{id_to}')
        return templates.TemplateResponse(name='createMessage.html',
                                          context={'request': request, 'id_to': id_to, 'path': path,
                                                   'id_from': id_from,'student': student})


@router.get('/feedbacks_vacancy')
async def get_feedbacks_vacancy_html(request: Request, id):
    feedbacks = await fetch(f'http://127.0.0.1:8000/api/feedbacks/?id_to={id}&path=1')
    for feedback in feedbacks:
        student = await fetch(f'http://127.0.0.1:8000/api/students/{feedback["id_from"]}')
        feedback['student'] = student['fio']
    return templates.TemplateResponse(name='feedback_vacancies.html',
                                      context={'request': request, "feedbacks": feedbacks})


@router.get('/messages_vacancy')
async def get_messages_vacancy_html(request: Request, id):
    messages = await fetch(f'http://127.0.0.1:8000/api/messages/ordered/?id_vacancy={id}&path_type=1')
    vacancy = await fetch(f'http://127.0.0.1:8000/api/vacancies/{id}')
    for message in messages:
        student = await fetch(f'http://127.0.0.1:8000/api/students/{message["id_student"]}')
        message['student'] = student['fio']
    return templates.TemplateResponse(name='message.html',
                                      context={'request': request, 'messages': messages, 'vacancy': vacancy})


@router.get('/messages_from_vacancy')
async def get_messages_from_vacancy_html(request: Request, id, user_data=Depends(get_me)):
    messages = await fetch(f'http://127.0.0.1:8000/api/messages/ordered/?id_student={user_data.student_id}&id_vacancy={id}&path_type=2')
    vacancy = await fetch(f'http://127.0.0.1:8000/api/vacancies/{id}')
    return templates.TemplateResponse(name='messageFromVacancy.html',
                                      context={'request': request, 'messages': messages, 'vacancy': vacancy, 'id_student': user_data.student_id})


