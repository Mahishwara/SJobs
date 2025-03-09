from pydantic import BaseModel, Field, field_validator
import datetime


class SApplication(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: datetime.date = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    id_status: int = Field(..., description='Ссылка на статус')





class SApplicationAdd(BaseModel):
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: str = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    id_status: int = Field(..., description='Ссылка на статус')

    @field_validator("date")
    @classmethod
    def validate_date(cls, values: str) -> datetime.date:
        valid_date = datetime.datetime.strptime(values, "%d.%m.%Y").date()
        if valid_date:
            return valid_date
        raise ValueError('Дата должны быть в формате ДД.ММ.ГГГГ')



class SApplicationUpd(BaseModel):
    id_status: int = Field(..., description='Ссылка на новый статус')