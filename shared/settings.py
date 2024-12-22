# if you want to use this settings, please include "overall" requirements.txt in your subproject
# it can be done by adding "-r ../shared/requirements/overall.txt" line to your requirements.txt

# don't forget to add shared requirements.txt to your Docker container!
from pathlib import Path

from dotenv import load_dotenv
from envparse import env

load_dotenv(env("DOTENV_FILE", default=None))


BASE_DIR = Path(__file__).resolve().parent.parent

# ENVIRONMENT = env("ENVIRONMENT")

# redis
# REDIS_HOST = env("REDIS_HOST", default="127.0.0.1")
# REDIS_DB = env("REDIS_DB", default="0")
# REDIS_PORT = env.int("REDIS_PORT", default=6379)
# REDIS_PROTOCOL = env("REDIS_PROTOCOL", default="redis")

# postgresql
PG_USERNAME = env("POSTGRES_USER", default="hobrus")
PG_PASSWORD = env("POSTGRES_PASSWORD", default="123321")
PG_HOST = env("DB_HOST", default="127.0.0.1")
PG_PORT = env.int("DB_PORT", default=5432)
PG_DB = env("POSTGRES_DB", default="EspressoNews")
PG_PROTOCOL = env("POSTGRES_PROTOCOL", default="postgresql+asyncpg")
PG_URI_QUERY = env("POSTGRES_URI_QUERY", default=str())

# # postgresql advertising
# PG_ADS_USERNAME = env("POSTGRES_ADS_USER", default="hobrus")
# PG_ADS_PASSWORD = env("POSTGRES_ADS_PASSWORD", default="123321")
# PG_ADS_HOST = env("DB_ADS_HOST", default="127.0.0.1")
# PG_ADS_PORT = env.int("DB_ADS_PORT", default=5432)
# PG_ADS_DB = env("POSTGRES_ADS_DB", default="EspressoNews")

# # mongo
# MONGO_USERNAME = env("MONGO_INITDB_ROOT_USERNAME", default="root")
# MONGO_PASSWORD = env("MONGO_INITDB_ROOT_PASSWORD", default="examplepassword")
# MONGO_HOST = env("MONGO_HOST", default="127.0.0.1")
# MONGO_PORT = env.int("MONGO_PORT", default=27017)
# MONGO_URI_QUERY = env("MONGO_URI_QUERY", default=str())
# MONGO_PROTOCOL = env("MONGO_PROTOCOL", default="mongodb")

# # rabbitmq
# RABBITMQ_USERNAME = env("RABBIT_USER", default="guest")
# RABBITMQ_PASSWORD = env("RABBIT_PASSWORD", default="guest")
# RABBITMQ_HOST = env("RABBIT_HOST", default="127.0.0.1")
# RABBITMQ_PORT = env.int("RABBIT_PORT", default=5672)
# RABBITMQ_PROTOCOL = env("RABBIT_PROTOCOL", default="amqp")
# RABBITMQ_URI_QUERY = env("RABBIT_URI_QUERY", default=str())