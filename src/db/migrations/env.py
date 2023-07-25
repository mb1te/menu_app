import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.engine.base import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from src.db.tables import BaseModel
from src.settings import get_settings

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = BaseModel.metadata


def do_run_migrations(connection: Connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_schemas=True,
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    settings = get_settings()
    engine = create_async_engine(settings.db_dsn)

    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)


asyncio.run(run_migrations_online())
