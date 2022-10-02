from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4


class TodoInput(BaseModel):
    name: str
    description: Optional[str]


class TodoOutput(BaseModel):
    id: UUID4
    name: str
    done: bool
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class TodoToPatch(BaseModel):
    name: Optional[str]
    description: Optional[str]
    done: Optional[bool]


class HttpError(BaseModel):
    detail: str
