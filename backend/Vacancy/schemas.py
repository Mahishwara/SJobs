from pydantic import BaseModel, Field, field_validator
import time
from datetime import date


class SVacancy(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str = Field(..., min_length=1, max_length=100, description='Наименование вакансии')
    description: str = Field(..., description='Дополнительная информации')
    date_begin: date = Field(..., description='Дата начала стажировки')
    date_end: date = Field(..., description='Дата окончания стажировки')
    level_skill: int = Field(..., description='Ссылка на нужный навык')
    salary: int = Field(..., description='Зарплата от')
    id_employer: int = Field(..., description='Идентификатор на работаделя')
    is_active: bool = Field(..., description='Активна/неактивна вакансия')




class SVacancyAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description='Наименование вакансии')
    description: str = Field(..., description='Дополнительная информации')
    date_begin: str = Field(..., description='Дата начала стажировки, в формате ГГГГ-ММ-ДД')
    date_end: str = Field(..., description='Дата окончания стажировки, в формате ГГГГ-ММ-ДД')
    level_skill: int = Field(..., description='Ссылка на нужный навык')
    salary: int = Field(..., description='Зарплата от')
    id_employer: int = Field(..., description='Идентификатор на работаделя')
    is_active: bool = Field(..., description='Активна/неактивна вакансия')


    @field_validator("salary")
    @classmethod
    def validate_salary(cls, values: int) -> int:
        if values > 0 and values < 999:
            return values
        raise ValueError('Оплата должна быть в диапазоне от 0 до 999 тысяч рублей')


    @field_validator('date_begin', 'date_end')
    @classmethod
    def validate_date(cls, values: str) -> date:
        validate_date = date.strftime(values, '%Y-%m-%d')
        if validate_date and validate_date > date.today():
            return datetime.strptime(values, '%Y-%m-%d').date()
        raise ValueError('Дата должна быть в формате ГГГГ-ММ-ДД и быть позднее сегоднешнего дня')


class SVacancyUpd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description='Новое наименование вакансии')
    description: str = Field(..., description='Новая дополнительная информации')
    date_begin: str = Field(..., description='Дата начала стажировки, в формате ГГГГ-ММ-ДД')
    date_end: str = Field(..., description='Дата окончания стажировки, в формате ГГГГ-ММ-ДД')
    level_skill: int = Field(..., description='Новая ссылка на нужный навык')
    salary: int = Field(..., description='Новая зарплата, можно указать: По соглосованию')
    id_employer: int = Field(..., description='Идентификатор на работаделя')
    is_active: bool = Field(..., description='Активна/неактивна вакансия')

    @field_validator("salary")
    @classmethod
    def validate_salary(cls, values: int) -> int:
        if values > 0 and values < 999:
            return values
        raise ValueError('Оплата должна быть в диапазоне от 0 до 999 тысяч рублей')


    @field_validator('date_begin', 'date_end')
    @classmethod
    def validate_date(cls, values: str) -> date:
        validate_date = date.strftime(values, '%Y-%m-%d')
        if validate_date and validate_date > date.today():
            return datetime.strptime(values, '%Y-%m-%d').date()
        raise ValueError('Дата должна быть в формате ГГГГ-ММ-ДД и быть позднее сегоднешнего дня')