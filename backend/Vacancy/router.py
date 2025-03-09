from fastapi import APIRouter, Depends
from backend.Vacancy.dao import VacancyDAO
from backend.Vacancy.rb import RBVacancy
from backend.Vacancy.schemas import SVacancy, SVacancyAdd, SVacancyUpd
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User


router = APIRouter(
    prefix='/vacancies',
    tags=['Вакансии']
)


@router.get("/", summary="Получить все вакансии")
async def get_all_vacancies(request_body: RBVacancy = Depends()) -> list[SVacancy]:
    return await VacancyDAO.get_all_objects(**request_body.to_dict())


@router.get("/find/", summary="Получить все вакансии")
async def find_vacancies(description) -> list[SVacancy]:
    return await VacancyDAO.find_objects(description)

@router.get("/{}", summary="Получить одину вакансию по ID")
async def get_vacancy_by_id(vacancy_id: int) -> SVacancy | dict:
    res = await VacancyDAO.get_object(id=vacancy_id)
    if res is None:
        return {'message': f'Вакансия с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новую вакансия')
async def register_vacancy(vacancy: SVacancyAdd) -> dict:
    check = await VacancyDAO.add(**vacancy.dict())
    if check:
        return {"message": "Вакансию успешно добавлена!", "vacancy": vacancy}
    else:
        return {"message": "Ошибка при добавлении вакансии!"}


@router.put("/update/{vacancy_id}", summary='Изменить вакансию по ID')
async def update_vacancy(vacancy_id, vacancy: SVacancyUpd) -> dict:
    check = await VacancyDAO.update(filter_by={'id': vacancy_id},
                                   name=vacancy.name, description=vacancy.description,
                                    close_date=vacancy.close_date,
                                    needed_skill=vacancy.needed_skill,
                                    salary=vacancy.salary)
    if check:
        return {"message": "Вакансия успешно обновлена!", "vacancy": vacancy}
    else:
        return {"message": "Ошибка при обновлении вакансии!"}


@router.delete("/delete/{vacancy_id}", summary='Удалить вакансию по ID')
async def delete_vacancy(vacancy_id) -> dict:
    check = await VacancyDAO.delete(id=vacancy_id)
    if check:
        return {"message": f"Вакансия успешно удалена!"}
    else:
        return {"message": "Ошибка при удалении вакансии!"}