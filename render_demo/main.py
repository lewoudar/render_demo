from typing import List

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from .config import settings
from .dependencies import get_todo, Pagination
from .models import Todo
from .schemas import TodoInput, TodoOutput, TodoToPatch, HttpError

app = FastAPI(title='Todo render_demo', version='1.0', description='Simple todo render_demo', redoc_url=None)


@app.post('/todos', response_model=TodoOutput, status_code=201)
async def create_todo(todo: TodoInput):
    return await Todo.create(name=todo.name, description=todo.description)


@app.get(
    '/todos/{todo_id}',
    response_model=TodoOutput,
    responses={
        404: {
            'description': 'todo not found',
            'model': HttpError
        }
    }
)
async def list_todo(todo: Todo = Depends(get_todo)):
    return TodoOutput.from_orm(todo)


@app.get('/todos', response_model=List[TodoOutput])
async def list_todos(p: Pagination = Depends()):
    todos = await Todo.all().limit(p.limit).offset(p.offset)
    return [TodoOutput.from_orm(todo) for todo in todos]


@app.patch(
    '/todos/{todo_id}',
    response_model=TodoOutput,
    responses={
        404: {
            'description': 'todo not found',
            'model': HttpError
        }
    }
)
async def update_todo(patched_todo: TodoToPatch, todo: Todo = Depends(get_todo)):
    await todo.update_from_dict(patched_todo.dict(exclude_unset=True))
    await todo.save()
    return todo


@app.delete('/todos/{todo_id}', status_code=204)
async def delete_todo(todo: Todo = Depends(get_todo)):
    await todo.delete()


@app.get('/search', description='Route to monitor app availability')
def health():
    return {'status': 'ok'}


register_tortoise(
    app,
    db_url=settings.database_url,
    modules={"models": ["render_demo.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
