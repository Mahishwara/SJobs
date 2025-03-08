from pydantic import BaseModel, Field


class SStudent(BaseModel):
    class Config:
        from_attributes = True

    id: int
    firstname: str = Field(..., min_length=3, max_length=25, description="Имя, от 3 до 25 символов")
    lastname: str = Field(..., min_length=3, max_length=35, description="Фамилия, от 3 до 35 символов")
    skill: str = Field(..., description="Укажите навык из предложенных")
    description: str = Field(..., description="Дополнительная информация")


class SStudentAdd(BaseModel):
    firstname: str = Field(..., min_length=3, max_length=25, description="Имя, от 3 до 25 символов")
    lastname: str = Field(..., min_length=3, max_length=35, description="Фамилия, от 3 до 35 символов")
    skill: str = Field(..., description="Укажите навык из предложенных")
    description: str = Field(..., description="Дополнительная информация")



class SStudentUpd(BaseModel):
    firstname: str = Field(..., min_length=3, max_length=25, description="Новое имя, от 3 до 25 символов")
    lastname: str = Field(..., min_length=3, max_length=35, description="Новая фамилия, от 3 до 35 символов")
    skill: str = Field(..., description="Укажите новый навык из предложенных")
    description: str = Field(..., description="Новая дополнительная информация")