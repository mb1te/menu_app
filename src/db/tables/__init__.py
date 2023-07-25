from src.db.tables.base import BaseModel
from src.db.tables.dish import DishModel
from src.db.tables.menu import MenuModel
from src.db.tables.submenu import SubmenuModel

__all__ = (
    "BaseModel",
    "MenuModel",
    "SubmenuModel",
    "DishModel",
)
