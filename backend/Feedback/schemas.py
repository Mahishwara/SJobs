from pydantic import BaseModel, Field


class SMessage(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description="Уникальный код получателя")
    id_employer: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., max_length=200, description="Отзыв работодателя о студенте")


class SMessageAdd(BaseModel):
    id_student: int = Field(..., description="Уникальный код получателя")
    id_employer: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., max_length=200, description="Отзыв работодателя о студенте")


class SMessageUpd(BaseModel):
    description: str = Field(..., max_length=200, description="Новый отзыв работодателя о студенте")