from backend.dao.base import BaseDAO
from backend.Vacancy.models import Vacancy


class VacancyDAO(BaseDAO):
    model = Vacancy