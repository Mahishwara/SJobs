from pydantic import BaseModel, Field


class SSkill(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str = Field(..., min_length=3, max_length=50, description="Название, от 3 до 50 символов")
    description: str = Field(..., description="Описание навыка")


class SSkillAdd(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Название, от 3 до 50 символов")
    description: str = Field(None, description="Описание навыка")



class SSkillUpd(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Новое название, от 3 до 50 символов")
    description: str = Field(None, description="Новое описание навыка")