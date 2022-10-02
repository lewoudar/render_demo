from tortoise import fields
from tortoise.models import Model


class Todo(Model):
    id = fields.UUIDField(pk=True)
    done = fields.BooleanField(default=False)
    name = fields.CharField(null=False, max_length=120)
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f'id={self.id}, created_at={self.created_at}, updated_at={self.updated_at}'
