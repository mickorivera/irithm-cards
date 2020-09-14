from playhouse.postgres_ext import AutoField, CharField, ForeignKeyField

from app.common.models import BaseSQLModel
from app.v1.user.models import UserModel


class ListModel(BaseSQLModel):
    id = AutoField(primary_key=True, index=True)
    author = ForeignKeyField(UserModel, backref="lists")
    title = CharField(max_length=256)

    class Meta(BaseSQLModel):
        table_name = "list"
