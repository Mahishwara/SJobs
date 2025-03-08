from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Vacancy(Base):
    __tablename__ = 'Vacancies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    publication_date: Mapped[str] = mapped_column(String(60), nullable=True)
    close_date: Mapped[str] = mapped_column(String(60), nullable=True)
    needed_skill: Mapped[int] = mapped_column(Integer, nullable=False)
    salary: Mapped[str] = mapped_column(String(100), nullable=False)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"name={self.name},"
                f"description={self.description},"
                f"publication_date={self.publication_date},"
                f"close_date={self.close_date},"
                f"needed_skill={self.needed_skill}"
                f"salary={self.salary},")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "publication_date": self.publication_date,
            "close_date": self.close_date,
            "needed_skill": self.needed_skill,
            "salary": self.salary,}