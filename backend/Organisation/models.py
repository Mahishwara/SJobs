from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Organisation(Base):
    __tablename__ = 'Organisations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    organization: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(60), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"name={self.name!r}, "
                f"organization={self.organization!r}, "
                f"email={self.email!r},"
                f"phone={self.phone!r},"
                f"adress={self.adress!r}, "
                f"description={self.description!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "organization": self.organization,
            "email": self.email,
            "phone": self.phone,
            "adress": self.adress,
            "description": self.description,}