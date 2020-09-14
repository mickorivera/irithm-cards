from playhouse.postgres_ext import AutoField, CharField, ForeignKeyField, DateTimeField

from app.common.models import BaseSQLModel
from app.v1.card.models import CardModel
from app.v1.user.models import UserModel


class CommentModel(BaseSQLModel):
    id = AutoField(primary_key=True, index=True)
    author = ForeignKeyField(UserModel, backref="comments")
    card = ForeignKeyField(CardModel, backref="comments")
    title = CharField(max_length=256)
    description = CharField(max_length=1024)
    date_updated = DateTimeField()

    class Meta(BaseSQLModel):
        table_name = "comments"


class CommentReplyModel(BaseSQLModel):
    id = AutoField(primary_key=True, index=True)
    author = ForeignKeyField(UserModel, backref="replies")
    comment = ForeignKeyField(CommentModel, backref="replies")
    content = CharField(max_length=256)
    date_updated = DateTimeField()

    class Meta(BaseSQLModel):
        table_name = "comment_replies"
