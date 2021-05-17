import uuid

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Index, String
from sqlalchemy.dialects.postgresql import UUID, INET
from sqlalchemy.sql.sqltypes import Boolean

from app.core.extensions import DB

Base = DB.Model
metadata = Base.metadata


class BaseMixin:
    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def add(self):
        DB.session.add(self)

    def save(self, commit=False):
        self.add()
        if commit:
            DB.session.commit()


class Search(Base, BaseMixin):
    __tablename__ = "searches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    time = Column(DateTime, nullable=False, default=datetime.utcnow)
    description = Column(String)
    location = Column(String)
    full_time = Column(Boolean)
    ip_address = Column(INET)

    def __repr__(self):
        return f"<ID {self.id}>"
