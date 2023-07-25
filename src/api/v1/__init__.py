from fastapi import APIRouter

from src.api.v1.dishes import router as dishes_router
from src.api.v1.menus import router as menus_router
from src.api.v1.submenus import router as submenus_router

router = APIRouter(prefix="/v1")
router.include_router(menus_router)
router.include_router(submenus_router)
router.include_router(dishes_router)

__all__ = ("router",)
