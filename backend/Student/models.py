from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.Interview.models import Interview
from backend.database import Base
import backend


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    skill: Mapped[int] = mapped_column(Integer, nullable=False)
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, firstname={self.firstname!r}, lastname={self.lastname!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            "description": self.description,
            "skill": self.skill,}
