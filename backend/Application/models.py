from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Application(Base):
    __tablename__ = 'Applications'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_student: Mapped[int] = mapped_column(ForeignKey("Students.id"), nullable=False)
    id_vacancy: Mapped[int] = mapped_column(ForeignKey("Vacancies.id"), nullable=False)
    date: Mapped[str] = mapped_column(String(60), nullable=True)
    status: Mapped[int] = mapped_column(ForeignKey("Statuses.id"), nullable=False)
    needed_skill: Mapped[int] = mapped_column(ForeignKey("Skills.id"), nullable=False)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"id_student={self.id_student},"
                f"id_vacancy={self.id_vacancy},"
                f"date={self.date},"
                f"status={self.status},"
                f"needed_skill={self.needed_skill}")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_student": self.id_student,
            "id_vacancy": self.id_vacancy,
            "date": self.date,
            "status": self.status,
            "needed_skill": self.needed_skill,}