from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.Interview.models import Interview
from backend.database import Base
import backend


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    post: Mapped[str] = mapped_column(String(50), nullable=False)
    level_skill: Mapped[int] = mapped_column(ForeignKey('level_skills.id'), nullable=False)
    speciality: Mapped[str] = mapped_column(String(200), nullable=False)
    course: Mapped[int] = mapped_column(Integer, nullable=False)
    ability: Mapped[str] = mapped_column(String(500), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, firstname={self.firstname!r},"
                f"lastname={self.lastname!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'post': self.post,
            'level_skill': self.level_skill,
            'speciality': self.speciality,
            'course': self.course,
            'ability': self.ability}
