from fastapi import APIRouter, Depends

from backend.Student.dao import StudentDAO
from backend.Student.rb import RBStudent
from backend.Student.schemas import SStudent, SStudentAdd, SStudentUpd
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User

router = APIRouter(
    prefix='/students',
    tags=['Студент']
)


@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list[SStudent]:
    return await StudentDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить одного студента по ID")
async def get_student_by_id(student_id: int) -> SStudent | dict:
    res = await StudentDAO.get_object(id=student_id)
    if res is None:
        return {'message': f'Студент с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить нового студента')
async def register_student(student: SStudentAdd) -> dict:
    check = await StudentDAO.add(**student.dict())
    if check:
        return {"message": "Студент успешно добавлена!", "Студент": student}
    else:
        return {"message": "Ошибка при добавлении категории!"}


@router.put("/update/{student_id}", summary='Изменить студента')
async def update_student(student_id, student: SStudentUpd,) -> dict:
    check = await StudentDAO.update(filter_by={'id': student_id},
                                    lastname=student.lastname,
                                    firstname=student.firstname,
                                    skill=student.skill,
                                    description=student.description)
    if check:
        return {"message": f"Данные студента успешно обновлены", "student": student}
    else:
        return {"message": "Ошибка при обновлении данных студента!"}


@router.delete("/delete/{student_id}", summary='Удалить студента по ID')
async def delete_student(request_body: RBStudent = Depends()) -> dict:
    check = await StudentDAO.delete(**request_body.to_dict())
    if check:
        return {"message": f"Студент успешно удален!"}
    else:
        return {"message": "Ошибка при удалении студента!"}