from sqlalchemy import text, Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database import Base, str_uniq, int_pk, str_null_true


class Student(Base):
    __tablename__ = 'Students'

    id: Mapped[int_pk] = Column(String(50))
    firstname: Mapped[str_uniq]
    lastname: Mapped[str_uniq]
    description: Mapped[str_null_true]
    skills: Mapped[list["Skill"]] = relationship("Skills", back_populates="category")
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
            "description": self.description}
