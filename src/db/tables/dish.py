from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.tables.base import BaseModel
from src.db.tables.submenu import SubmenuModel


class DishModel(BaseModel):
    __tablename__ = "dish"
    entity = "dish"

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    submenu_id: Mapped[UUID] = mapped_column(
        ForeignKey("submenu.id", ondelete="CASCADE")
    )
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=False)

    submenu: Mapped[SubmenuModel] = relationship(back_populates="dishes")
