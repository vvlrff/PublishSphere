from datetime import datetime
from typing import Protocol, Optional
from pydantic import BaseModel


class ActionStatus(BaseModel):
    success: bool


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: datetime

    class Config:
        from_attributes = True


class CreatePostPayload(BaseModel):
    title: str
    content: str
    author: str


class PostStorage(Protocol):
    async def create_post(self, data: CreatePostPayload) -> PostSchema: ...
    async def get_post(self, post_id: int) -> Optional[PostSchema]: ...
    async def get_all_posts(self) -> list[PostSchema]: ...
    async def delete_post(self, post_id: int) -> ActionStatus: ...
