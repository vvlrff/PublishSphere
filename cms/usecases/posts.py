from typing import Optional
from pydantic import BaseModel
from cms.common.protocols import PostStorage, PostSchema, CreatePostPayload


class CreatePostInput(BaseModel):
    title: str
    content: str
    author: str


class CreatePostOutput(BaseModel):
    post: PostSchema


class DeletePostOutput(BaseModel):
    success: bool


class GetPostInput(BaseModel):
    post_id: int


class CreatePost:
    def __init__(self, storage: PostStorage):
        self.storage = storage

    async def __call__(self, data: CreatePostInput) -> CreatePostOutput:
        post = await self.storage.create_post(CreatePostPayload(**data.model_dump()))
        return CreatePostOutput(post=post)


class GetPost:
    def __init__(self, storage: PostStorage):
        self.storage = storage

    async def __call__(self, data: GetPostInput) -> Optional[PostSchema]:
        return await self.storage.get_post(data.post_id)


class GetAllPosts:
    def __init__(self, storage: PostStorage):
        self.storage = storage

    async def __call__(self) -> Optional[list[PostSchema]]:
        return await self.storage.get_all_posts()


class DeletePost:
    def __init__(self, storage: PostStorage):
        self.storage = storage

    async def __call__(self, data: GetPostInput) -> DeletePostOutput:
        return await self.storage.delete_post(data.post_id)
