from pydantic import BaseModel, Field, field_validator
import re


class SOrganisation(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str = Field(..., min_length=3, max_length=50, description='Наименование организации, от 3 до 50 символов')
    description: str = Field(..., max_length=100, description='Дополнительная информация')
    adress: str = Field(..., max_length=100, description='Адресс осноного офиса')
    email: str = Field(..., max_length=50, description='Электронная почта горячей линии')
    phone: str = Field(..., max_length=20, description="Номер телефона горячей линии в международном формате, начинающийся с '+'")





class SOrganisationAdd(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description='Наименование организации, от 3 до 50 символов')
    description: str = Field(..., max_length=100, description='Дополнительная информация')
    adress: str = Field(..., max_length=100, description='Адресс осноного офиса')
    email: str = Field(..., max_length=50, description='Электронная почта горячей линии')
    phone: str = Field(..., max_length=20,
                       description="Номер телефона горячей линии в международном формате, начинающийся с '+'")

    @field_validator("phone")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{11}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать 11 цифр')
        return values



class SOrganisationUpd(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description='Новое наименование организации, от 3 до 50 символов')
    description: str = Field(..., max_length=100, description='Новая дополнительная информация')
    adress: str = Field(..., max_length=100, description='Новый адресс осноного офиса')
    email: str = Field(..., max_length=50, description='Новая электронная почта горячей линии')
    phone: str = Field(..., max_length=20,
                       description="Новый номер телефона горячей линии в международном формате, начинающийся с '+'")