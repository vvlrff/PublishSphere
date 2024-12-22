from typing import AsyncIterator
from dishka import Provider, alias, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from urllib.parse import urlunsplit
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel

from cms.adapters.postgres import PostgresAdapter
from cms.common.protocols import PostStorage
from cms.usecases.posts import CreatePost, DeletePost, GetPost, GetAllPosts
from shared import settings


def get_pg_uri(
    username=settings.PG_USERNAME,
    password=settings.PG_PASSWORD,
    host=settings.PG_HOST,
    port=settings.PG_PORT,
    db=settings.PG_DB,
    protocol=settings.PG_PROTOCOL,
    uri_query=settings.PG_URI_QUERY,
):
    return urlunsplit(
        (protocol, f"{username}:{password}@{host}:{port}", db, uri_query, str())
    )


class ProtocolsProvider(Provider):
    post_storage = alias(source=PostgresAdapter, provides=PostStorage)


class PostgresqlPoolOptions(BaseModel):
    pool_size: int = 600
    max_overflow: int = 100
    pool_timeout: int = 10
    pool_pre_ping: bool = True


class PostgresProvider(Provider):
    @provide(scope=Scope.APP)
    async def provide_pool_options(self) -> PostgresqlPoolOptions:
        return PostgresqlPoolOptions()

    @provide(scope=Scope.APP)
    async def provide_async_engine(
        self, options: PostgresqlPoolOptions
    ) -> AsyncIterator[async_sessionmaker]:
        engine = create_async_engine(get_pg_uri(), **options.model_dump())
        pool = async_sessionmaker(bind=engine)
        yield pool
        await engine.dispose()

    @provide(scope=Scope.REQUEST)
    async def provide_async_session(
        self, pool: async_sessionmaker
    ) -> AsyncIterator[AsyncSession]:
        async with pool() as session:
            try:
                yield session
            except SQLAlchemyError as exc:
                await session.rollback()
                raise exc
            else:
                await session.commit()

    postgres_adapter = provide(PostgresAdapter, scope=Scope.REQUEST)


class ApiUseCaseProvider(Provider):
    create_post = provide(CreatePost, scope=Scope.REQUEST)
    get_post = provide(GetPost, scope=Scope.REQUEST)
    get_all_post = provide(GetAllPosts, scope=Scope.REQUEST)
    delete_post = provide(DeletePost, scope=Scope.REQUEST)
