from pydantic import BaseModel, Field


class SMessage(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_to: int = Field(..., description="Уникальный код получателя")
    id_from: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., description="Сообщение")
    path_type: int = Field(..., description="Путь сообщения: 1 = студент-вакансия; 2 = вакансия-студент")


class SMessageAdd(BaseModel):
    id_to: int = Field(..., description="Уникальный код получателя")
    id_from: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., description="Сообщение")
    path_type: int = Field(..., description="Путь сообщения: 1 = студент-вакансия; 2 = вакансия-студент")