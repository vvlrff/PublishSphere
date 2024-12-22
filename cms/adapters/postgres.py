from typing import Optional
from sqlalchemy import delete, select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from cms.common.protocols import (
    CreatePostPayload,
    PostSchema,
    PostStorage,
    ActionStatus,
)
from shared.models import Post


class PostgresAdapter(PostStorage):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_post(self, data: CreatePostPayload) -> PostSchema:
        stmt = (
            insert(Post)
            .values(**data.model_dump())
            .returning(Post.id, Post.title, Post.content, Post.author, Post.created_at)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        post = result.one()
        return PostSchema.model_validate(post)

    async def get_post(self, post_id: int) -> Optional[PostSchema]:
        stmt = select(Post).where(Post.id == post_id)
        result = await self.session.execute(stmt)
        post = result.scalar_one_or_none()
        return PostSchema.model_validate(post) if post else None

    async def get_all_posts(self) -> list[PostSchema]:
        stmt = select(Post)
        result = await self.session.execute(stmt)
        return [PostSchema.model_validate(post) for post in result.scalars().all()]

    async def delete_post(self, post_id: int) -> ActionStatus:
        exists_stmt = select(Post).where(Post.id == post_id)
        result = await self.session.execute(exists_stmt)
        post = result.scalar_one_or_none()

        if not post:
            return ActionStatus(success=False)

        stmt = delete(Post).where(Post.id == post_id)
        await self.session.execute(stmt)
        await self.session.commit()
        return ActionStatus(success=True)
