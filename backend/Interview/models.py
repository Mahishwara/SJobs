from sqlalchemy import String, Integer,DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base
from datetime import datetime


class Interview(Base):
    __tablename__ = 'interview'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_student: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    id_vacancy: Mapped[int] = mapped_column(ForeignKey("vacancies.id"), nullable=False)
    date: Mapped[datetime] = mapped_column(DATETIME, nullable=True)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"id_student={self.id_student!r}, "
                f"id_vacancy={self.id_vacancy!r}, "
                f"date={self.date!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_student": self.id_student,
            "id_vacancy": self.id_vacancy,
            "date": self.date,}