from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.tables.base import BaseModel

if TYPE_CHECKING:
    from src.db.tables.submenu import SubmenuModel


class MenuModel(BaseModel):
    __tablename__ = "menu"
    entity = "menu"

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    submenus: Mapped[list["SubmenuModel"]] = relationship(
        back_populates="menu", cascade="all,delete", lazy="joined"
    )

    @hybrid_property
    def submenus_count(self) -> int:
        return len(self.submenus)

    @hybrid_property
    def dishes_count(self) -> int:
        return sum(submenu.dishes_count for submenu in self.submenus)
