from pydantic import BaseModel, Field, field_validator
from datetime import date


class SApplication(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: date = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    id_status: int = Field(..., description='Ссылка на статус')





class SApplicationAdd(BaseModel):
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: str = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    id_status: int = Field(..., description='Ссылка на статус')

    @field_validator("date")
    @classmethod
    def validate_date(cls, values: str) -> str:
        valid_date = datetime.strptime(values, "%Y-%m-%d").date()
        if valid_date:
            return values
        raise ValueError('Дата должны быть в формате ДД.ММ.ГГГГ')



class SApplicationUpd(BaseModel):
    id_status: int = Field(..., description='Ссылка на новый статус')