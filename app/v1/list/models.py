from playhouse.postgres_ext import (
    AutoField,
    CharField,
    ForeignKeyField,
    DateTimeField,
)

from app.common.models import BaseSQLModel
from app.v1.user.models import UserModel


class ListModel(BaseSQLModel):
    id = AutoField()
    author = ForeignKeyField(UserModel, backref="lists")
    title = CharField(max_length=256)
    date_created = DateTimeField(null=True)
    date_updated = DateTimeField(null=True)

    class Meta(BaseSQLModel):
        table_name = "lists"
