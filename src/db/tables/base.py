from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase, AsyncAttrs):
    __abstract__ = True
    type_annotation_map = {dict: JSONB, datetime: DateTime(timezone=True)}
