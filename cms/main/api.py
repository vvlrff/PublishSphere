from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from cms.api.routers import routers
from cms.main.ioc import PostgresProvider, ApiUseCaseProvider, ProtocolsProvider


def create_app():
    app = FastAPI(docs_url="/docs")

    for router in routers:
        app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    container = make_async_container(
        PostgresProvider(), ApiUseCaseProvider(), ProtocolsProvider()
    )

    setup_dishka(container, app)

    return app
