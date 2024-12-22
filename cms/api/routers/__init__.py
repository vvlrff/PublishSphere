from .posts import posts_router


routers = [
    posts_router
]


__all__ = (
    "routers",
    "posts_router",
)
