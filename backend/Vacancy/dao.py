from dao.base import BaseDAO
from Vacancy.models import Vacancy


class VacancyDAO(BaseDAO):
    model = Vacancy