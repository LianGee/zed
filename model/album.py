from sqlalchemy import String, Column, Boolean

from model.base import BaseModel
from model.db import Model


class Album(Model, BaseModel):
    __tablename__ = 'album'

    user_name = Column(String)
    title = Column(String)
    description = Column(String)
    cover_url = Column(String)
    is_public = Column(Boolean, default=False)
