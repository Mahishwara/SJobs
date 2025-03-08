from backend.dao.base import BaseDAO
from backend.Organisation.models import Organisation


class OrganisationDAO(BaseDAO):
    model = Organisation