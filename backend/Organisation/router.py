from fastapi import APIRouter, Depends

from backend.Organisation.dao import OrganisationDAO
from backend.Organisation.rb import RBOrganisation
from backend.Organisation.schemas import SOrganisation, SOrganisationAdd, SOrganisationUpd
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User


router = APIRouter(
    prefix='/organisations',
    tags=['Организация']
)


@router.get("/", summary="Получить все организации")
async def get_all_organisation(request_body: RBOrganisation = Depends()) -> list[SOrganisation]:
    return await OrganisationDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить одну организацию по ID")
async def get_organisation_by_id(organisation_id: int) -> SOrganisation | dict:
    res = await OrganisationDAO.get_object(id=organisation_id)
    if res is None:
        return {'message': f'Организация с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новую организацию')
async def register_organisation(organisation: SOrganisationAdd) -> dict:
    check = await OrganisationDAO.add(**organisation.dict())
    if check:
        return {"message": "Организация успешно добавлена!", "organisation": organisation}
    else:
        return {"message": "Ошибка при добавлении организации!"}


@router.put("/update/{organisation_id}", summary='Изменить организацию по ID')
async def update_organisation(organisation_id, organisation: SOrganisationUpd) -> dict:
    check = await OrganisationDAO.update(filter_by={'id': organisation_id},
                                   name=organisation.name, description=organisation.description)
    if check:
        return {"message": "Организация успешно обновлена!", "organisation": organisation}
    else:
        return {"message": "Ошибка при обновлении организации!"}


@router.delete("/delete/{organisation_id}", summary='Удалить навык по ID')
async def delete_category(organisation_id) -> dict:
    check = await OrganisationDAO.delete(id=organisation_id)
    if check:
        return {"message": f"Организация успешно удалена!"}
    else:
        return {"message": "Ошибка при удалении организации!"}