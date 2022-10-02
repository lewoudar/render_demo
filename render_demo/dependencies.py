from fastapi import HTTPException, Query

from render_demo.models import Todo


async def get_todo(todo_id: str) -> Todo:
    todo = await Todo.get_or_none(pk=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='todo not found')

    return todo


class Pagination:
    def __init__(
            self,
            page: int = Query(1, description='number of the page to fetch', ge=1),
            page_size: int = Query(50, description='number of items per page', ge=1, le=100)
    ):
        self.limit = page_size
        self.offset = (page * page_size) - page_size
