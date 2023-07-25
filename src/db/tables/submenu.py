from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.tables.base import BaseModel
from src.db.tables.menu import MenuModel

if TYPE_CHECKING:
    from src.db.tables.dish import DishModel


class SubmenuModel(BaseModel):
    __tablename__ = "submenu"
    entity = "submenu"

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    menu_id: Mapped[UUID] = mapped_column(ForeignKey("menu.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    menu: Mapped[MenuModel] = relationship(back_populates="submenus")
    dishes: Mapped[list["DishModel"]] = relationship(
        back_populates="submenu", cascade="all,delete", lazy="joined"
    )

    @hybrid_property
    def dishes_count(self) -> int:
        return len(self.dishes)
