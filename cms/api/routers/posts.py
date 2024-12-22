from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, HTTPException

from cms.common.protocols import ActionStatus, PostSchema
from cms.usecases.posts import (
    CreatePost,
    GetPost,
    CreatePostInput,
    GetPostInput,
    GetAllPosts,
    DeletePost,
)

posts_router = APIRouter(route_class=DishkaRoute, tags=["Posts"])


@posts_router.post("/posts/", response_model=PostSchema)
async def create_post(
    data: CreatePostInput, create_post: FromDishka[CreatePost]
) -> PostSchema:
    result = await create_post(data)
    return result.post


@posts_router.get("/posts/{post_id}", response_model=PostSchema)
async def get_post(post_id: int, get_post: FromDishka[GetPost]) -> PostSchema:
    result = await get_post(GetPostInput(post_id=post_id))
    if not result:
        raise HTTPException(status_code=404, detail="Post not found")
    return result


@posts_router.get("/posts", response_model=list[PostSchema])
async def get_post(get_all_post: FromDishka[GetAllPosts]) -> PostSchema:
    result = await get_all_post()
    if not result:
        raise HTTPException(status_code=404, detail="Posts not found")
    return result


@posts_router.delete("/posts/{post_id}", response_model=ActionStatus)
async def delete_post(
    post_id: int, delete_post: FromDishka[DeletePost]
) -> ActionStatus:
    result = await delete_post(GetPostInput(post_id=post_id))
    if not result.success:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    return result
