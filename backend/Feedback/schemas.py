from pydantic import BaseModel, Field


class SFeedback(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description="Уникальный код получателя")
    id_employer: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., max_length=200, description="Отзыв работодателя о студенте")


class SFeedbackAdd(BaseModel):
    id_student: int = Field(..., description="Уникальный код получателя")
    id_employer: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., max_length=200, description="Отзыв работодателя о студенте")


class SFeedbackUpd(BaseModel):
    description: str = Field(..., max_length=200, description="Новый отзыв работодателя о студенте")