from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shared.dbs.postgresql.get_pg_uri import get_pg_uri

sync_engine = create_engine(get_pg_uri(protocol='postgresql+psycopg2'), pool_pre_ping=True)

sync_session = sessionmaker(sync_engine)
