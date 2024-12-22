from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from shared.dbs.postgresql.get_pg_uri import get_pg_uri, get_pg_uri_for_ads

async_engine = create_async_engine(get_pg_uri(), pool_size=600, max_overflow=100, pool_timeout=10, pool_pre_ping=True)

async_session = async_sessionmaker(async_engine, expire_on_commit=False)
async_session_noauto = async_sessionmaker(async_engine, autocommit=False, autoflush=False, expire_on_commit=False)

async_engine = create_async_engine(get_pg_uri_for_ads(), pool_size=600, max_overflow=100, pool_timeout=10, pool_pre_ping=True)
async_session_noauto_ads = async_sessionmaker(async_engine, autocommit=False, autoflush=False, expire_on_commit=False)