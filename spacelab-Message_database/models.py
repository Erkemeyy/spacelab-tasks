from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    user = fields.ForeignKeyField("models.User", related_name="posts")
