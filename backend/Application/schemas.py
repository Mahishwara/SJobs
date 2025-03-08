from pydantic import BaseModel, Field
import time


class SApplication(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: str = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    status: int = Field(..., description='Ссылка на статус')


    @field_validator("date")
    @classmethod
    def validate_date(cls, values: str) -> str:
        if time.strptime(values, '%d.%m.%Y'):
            return valid_date
        raise ValueError('Дата должны быть в формате ДД.ММ.ГГГГ')


class SApplicationAdd(BaseModel):
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: str = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    status: int = Field(..., description='Ссылка на статус')


class SEmployerUpd(BaseModel):
    status: int = Field(..., description='Ссылка на новый статус')