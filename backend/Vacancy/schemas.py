from pydantic import BaseModel, Field
import time


class SVacancy(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str = Field(..., min_length=1, max_length=100, description='Наименование вакансии')
    description: str = Field(..., description='Дополнительная информации')
    publication_date: str = Field(..., description='Дата публикации в формате ДД.ММ.ГГГГ')
    close_date: str = Field(..., description='Дата закрытия в формате ДД.ММ.ГГГГ')
    needed_skill: int = Field(..., description='Ссылка на нужный навык')
    salary: str = Field(..., description='Зарплата, можно указать: По соглосованию')


    @field_validator(["publication_date", 'close_date'])
    @classmethod
    def validate_date(cls, values: str) -> str:
        if time.strptime(values, '%d.%m.%Y'):
            return valid_date
        raise ValueError('Дата должны быть в формате ДД.ММ.ГГГГ')


class SVacancyAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description='Наименование вакансии')
    description: str = Field(..., description='Дополнительная информации')
    publication_date: str = Field(..., description='Дата публикации в формате ДД.ММ.ГГГГ')
    close_date: str = Field(..., description='Дата закрытия в формате ДД.ММ.ГГГГ')
    needed_skill: int = Field(..., description='Ссылка на нужный навык')
    salary: str = Field(..., description='Зарплата, можно указать: По соглосованию')


class SVacancyUpd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description='Новое наименование вакансии')
    description: str = Field(..., description='Новая дополнительная информации')
    close_date: str = Field(..., description='Новая дата закрытия в формате ДД.ММ.ГГГГ')
    needed_skill: int = Field(..., description='Новая ссылка на нужный навык')
    salary: str = Field(..., description='Новая зарплата, можно указать: По соглосованию')