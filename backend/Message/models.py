from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_student: Mapped[int] = mapped_column(ForeignKey('students.id'), nullable=False)
    id_vacancy: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    path_type: Mapped[int] = mapped_column(Integer, nullable=True)
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, id_student={self.id_student}, id_vacancy={self.id_vacancy}, path_type={self.path_type}, description={self.description!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_student": self.id_student,
            "id_vacancy": self.id_vacancy,
            "path_type": self.path_type,
            "description": self.description,}