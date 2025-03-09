from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class SInterview(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description="Уникальный код студента")
    id_vacancy: int = Field(..., description="Уникальный код вакансии")
    date: datetime = Field(..., description="Дата собеседования по вакансии")


class SInterviewAdd(BaseModel):
    id_student: int = Field(..., description="Уникальный код студента")
    id_vacancy: int = Field(..., description="Уникальный код вакансии")
    date: datetime = Field(..., description="Дата собеседования по вакансии")

    @field_validator("date")
    @classmethod
    def validate_date(cls, values: str) -> str:
        if datetime.strptime(values, '%d.%m.%Y %H:%M'):
            return values
        raise ValueError('Даты должны быть в формате ДД.ММ.ГГГГ ЧЧ:ММ')


class SInterviewUpd(BaseModel):
    date: datetime = Field(..., description="Дата собеседования по вакансии")

    @field_validator("date")
    @classmethod
    def validate_date(cls, values: str) -> str:
        if datetime.strptime(values, '%d.%m.%Y %H:%M'):
            return values
        raise ValueError('Даты должны быть в формате ДД.ММ.ГГГГ ЧЧ:ММ')