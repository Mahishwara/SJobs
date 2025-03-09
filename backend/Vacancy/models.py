from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base
from datetime import datetime

class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    post: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    publication_date: Mapped[datetime] = mapped_column(DATETIME, nullable=True, default=datetime.now)
    level_skill: Mapped[int] = mapped_column(ForeignKey('level_skills.id'), nullable=False)
    salary: Mapped[int] = mapped_column(Integer, nullable=False)
    id_employer: Mapped[int] = mapped_column(ForeignKey('employers.id'), nullable=False)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"name={self.name},"
                f"description={self.description},"
                f"publication_date={self.publication_date},"
                f"level_skill={self.level_skill}"
                f"salary={self.salary},"
                f"id_employer={self.id_employer})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "publication_date": self.publication_date,
            "level_skill": self.level_skill,
            "salary": self.salary,
            "id_employer": self.id_employer,}