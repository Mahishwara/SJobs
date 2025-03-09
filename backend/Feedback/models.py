from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Feedback(Base):
    __tablename__ = 'Feedbacks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_student: Mapped[int] = mapped_column(Integer, nullable=False)
    id_employer: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"id_student={self.id_student!r}, "
                f"id_employer={self.id_employer!r}, "
                f"description={self.description!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_student": self.id_student,
            "id_employer": self.id_employer,
            "description": self.description,}