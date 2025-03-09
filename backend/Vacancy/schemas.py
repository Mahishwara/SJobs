from pydantic import BaseModel, Field, field_validator
import time


class SVacancy(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str = Field(..., min_length=1, max_length=100, description='Наименование вакансии')
    description: str = Field(..., description='Дополнительная информации')
    level_skill: int = Field(..., description='Ссылка на нужный навык')
    salary: int = Field(..., description='Зарплата от')
    id_employer: int = Field(..., description='Идентификатор на работаделя')



class SVacancyAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description='Наименование вакансии')
    description: str = Field(..., description='Дополнительная информации')
    level_skill: int = Field(..., description='Ссылка на нужный навык')
    salary: int = Field(..., description='Зарплата от')
    id_employer: int = Field(..., description='Идентификатор на работаделя')

    @field_validator("salary")
    @classmethod
    def validate_salary(cls, values: int) -> int:
        if values > 0 and values < 999:
            return values
        raise ValueError('Оплата должна быть в диапазоне от 0 до 999 тысяч рублей')

class SVacancyUpd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description='Новое наименование вакансии')
    description: str = Field(..., description='Новая дополнительная информации')
    level_skill: int = Field(..., description='Новая ссылка на нужный навык')
    salary: int = Field(..., description='Новая зарплата, можно указать: По соглосованию')
    id_employer: int = Field(..., description='Идентификатор на работаделя')

    @field_validator("salary")
    @classmethod
    def validate_salary(cls, values: int) -> int:
        if values > 0 and values < 999:
            return values
        raise ValueError('Оплата должна быть в диапазоне от 0 до 999 тысяч рублей')