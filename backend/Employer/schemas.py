from pydantic import BaseModel, Field, field_validator
import re

class SEmployer(BaseModel):
    class Config:
        from_attributes = True

    name: str = Field(..., min_length=3, max_length=50, description="Название работодателя, от 3 до 50 символов")
    organization: int = Field(..., description='Идентификатор организации')
    email: str = Field(..., description='Личная электронная почта')
    phone: str = Field(..., description="Личный номер телефона в международном формате, начинающийся с '+'")
    description: str = Field(..., description='Дополнительная информация')




class SEmployerAdd(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Название работодателя, от 3 до 50 символов")
    organization: int = Field(..., description='Идентификатор организации')
    email: str = Field(..., description='Личная электронная почта')
    phone: str = Field(..., description="Личный номер телефона в международном формате, начинающийся с '+'")
    description: str = Field(..., description='Дополнительная информация')

    @field_validator("phone")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{11}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 11 цифр')
        return values


class SEmployerUpd(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Новое название работодателя, от 3 до 50 символов")
    organization: int = Field(..., description='Идентификатор организации')
    email: str = Field(..., description='Новая личная электронная почта')
    phone: str = Field(..., description="Новый личный номер телефона в международном формате, начинающийся с '+'")
    description: str = Field(..., description='Новая дополнительная информация')