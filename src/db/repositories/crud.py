from typing import Generic, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.tables.base import BaseModel
from src.exceptions import NotFound

Model = TypeVar("Model", bound=BaseModel)


class BaseCRUDRepository(Generic[Model]):
    def __init__(self, session: AsyncSession, model: BaseModel):
        self.session = session
        self.model = model

    async def commit(self):
        await self.session.commit()

    async def get(self, item_id: str, **kwargs) -> Model:
        try:
            query = select(self.model).filter_by(id=item_id, **kwargs)
            expr = await self.session.execute(query)
            return expr.unique().scalar_one()
        except NoResultFound:
            raise NotFound(entity=self.model.entity)

    async def get_all(self, **kwargs) -> list[Model]:
        query = select(self.model).filter_by(**kwargs)
        expr = await self.session.execute(query)
        return expr.scalars().unique().fetchall()

    async def create(self, **kwargs) -> Model:
        query = insert(self.model).values(**kwargs).returning(self.model)
        expr = await self.session.execute(query)
        return expr.unique().scalar_one()

    async def update(self, item_id: int, **kwargs) -> Model:
        query = (
            update(self.model)
            .filter_by(id=item_id)
            .values(**kwargs)
            .returning(self.model)
        )
        expr = await self.session.execute(query)
        return expr.unique().scalar_one()

    async def delete(self, item_id: int, **kwargs):
        query = delete(self.model).filter_by(id=item_id, **kwargs)
        await self.session.execute(query)
