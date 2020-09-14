from playhouse.postgres_ext import AutoField, CharField, ForeignKeyField, DateTimeField

from app.common.models import BaseSQLModel
from app.v1.list.models import ListModel
from app.v1.user.models import UserModel


class CardModel(BaseSQLModel):
    id = AutoField(primary_key=True, index=True)
    author = ForeignKeyField(UserModel, backref="cards")
    list = ForeignKeyField(ListModel, backref="cards")
    title = CharField(max_length=256)
    description = CharField(max_length=1024)
    date_updated = DateTimeField()

    class Meta(BaseSQLModel):
        table_name = "cards"
