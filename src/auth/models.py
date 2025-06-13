from fastapi_users.db import SQLAlchemyBaseUserTable

from src.models import Base
from src.mixins import IdIntMixin


class User(Base, IdIntMixin, SQLAlchemyBaseUserTable[int]):
    pass
