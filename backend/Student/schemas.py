from pydantic import BaseModel, Field, field_validator


class SStudent(BaseModel):
    class Config:
        from_attributes = True

    id: int
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., description='Уровень владения')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course:  int = Field(...,description='Номер курса')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")


class SStudentAdd(BaseModel):
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., description='Уровень владения')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course: int = Field(..., description='Номер курса')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")

    @field_validator("course")
    @classmethod
    def validate_salary(cls, values: int) -> int:
        if values > 0 and values < 7:
            return values
        raise ValueError('Курс должен быть в диапазоне от 1 до 6')



class SStudentUpd(BaseModel):
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., description='Уровень владения')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course: int = Field(..., description='Номер курса')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")


    @field_validator("course")
    @classmethod
    def validate_course(cls, values: int) -> int:
        if values > 0 and values < 7:
            return values
        raise ValueError('Курс должен быть в диапазоне от 1 до 6')