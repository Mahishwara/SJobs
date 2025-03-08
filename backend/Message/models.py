from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Message(Base):
    __tablename__ = 'Messages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_to: Mapped[int] = mapped_column(Integer, nullable=False)
    id_from: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, id_to={self.id_to!r}, id_from={self.id_from!r}, description={self.description!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'id_to': self.id_to,
            'id_from': self.id_from,
            "description": self.description,}