from fastapi import APIRouter, Depends

from backend.Skill.dao import SkillDAO
from backend.Skill.rb import RBSkill
from backend.Skill.schemas import SSkill, SSkillAdd, SSkillUpd
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User


router = APIRouter(
    prefix='/skills',
    tags=['Навык']
)


@router.get("/", summary="Получить все навыки")
async def get_all_skills(request_body: RBSkill = Depends()) -> list[SSkill]:
    return await SkillDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить один навык по ID")
async def get_skill_by_id(skill_id: int) -> SSkill | dict:
    res = await SkillDAO.get_object(id=skill_id)
    if res is None:
        return {'message': f'Навык с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новый навык')
async def register_skill(skill: SSkillAdd) -> dict:
    check = await SkillDAO.add(**skill.dict())
    if check:
        return {"message": "Навык успешно добавлен!", "skill": skill}
    else:
        return {"message": "Ошибка при добавлении навыка!"}


@router.put("/update/{skill_id}", summary='Изменить навык')
async def update_skill(skill_id, skill: SSkillUpd) -> dict:
    check = await SkillDAO.update(filter_by={'id': skill_id},
                                   name=skill.name, description=skill.description)
    if check:
        return {"message": "Навык успешно обновлен!", "skill": skill}
    else:
        return {"message": "Ошибка при обновлении навыка!"}


@router.delete("/delete/{skill_id}", summary='Удалить навык по ID')
async def delete_skill(skill_id) -> dict:
    check = await SkillDAO.delete(id=skill_id)
    if check:
        return {"message": f"Навык успешно удален!"}
    else:
        return {"message": "Ошибка при удалении навыка!"}