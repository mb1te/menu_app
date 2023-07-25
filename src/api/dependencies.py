from typing import TypeVar

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.db.repositories.crud import BaseCRUDRepository
from src.db.tables.dish import DishModel
from src.db.tables.menu import MenuModel
from src.db.tables.submenu import SubmenuModel
from src.settings import AppSettings

MenuRepo = TypeVar("MenuRepo", bound=BaseCRUDRepository[MenuModel])
SubmenuRepo = TypeVar("SubmenuRepo", bound=BaseCRUDRepository[SubmenuModel])
DishRepo = TypeVar("DishRepo", bound=BaseCRUDRepository[DishModel])


def get_engine(settings: AppSettings) -> AsyncEngine:
    return create_async_engine(
        settings.db_dsn, echo=settings.fastapi_debug, echo_pool=settings.fastapi_debug
    )


async def get_session(engine: AsyncEngine = Depends(get_engine)) -> AsyncSession:
    create_session = async_sessionmaker(bind=engine, expire_on_commit=False)
    async with create_session() as session:
        yield session


async def get_menu_repo(session: AsyncSession = Depends(get_session)) -> MenuRepo:
    return BaseCRUDRepository(session=session, model=MenuModel)


async def get_submenu_repo(session: AsyncSession = Depends(get_session)) -> SubmenuRepo:
    return BaseCRUDRepository(session=session, model=SubmenuModel)


async def get_dish_repo(session: AsyncSession = Depends(get_session)) -> DishRepo:
    return BaseCRUDRepository(session=session, model=DishModel)
