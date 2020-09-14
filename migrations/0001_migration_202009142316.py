# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class UserModel(peewee.Model):
    username = CharField(index=True, max_length=16, primary_key=True)
    email_address = CharField(max_length=256, unique=True)
    password = CharField(max_length=1024)
    class Meta:
        table_name = "user"


@snapshot.append
class ListModel(peewee.Model):
    author = snapshot.ForeignKeyField(backref='lists', index=True, model='usermodel')
    title = CharField(max_length=256)
    class Meta:
        table_name = "list"


@snapshot.append
class CardModel(peewee.Model):
    author = snapshot.ForeignKeyField(backref='cards', index=True, model='usermodel')
    list = snapshot.ForeignKeyField(backref='cards', index=True, model='listmodel')
    title = CharField(max_length=256)
    description = CharField(max_length=1024)
    class Meta:
        table_name = "card"


@snapshot.append
class CommentModel(peewee.Model):
    author = snapshot.ForeignKeyField(backref='comments', index=True, model='usermodel')
    card = snapshot.ForeignKeyField(backref='comments', index=True, model='cardmodel')
    title = CharField(max_length=256)
    description = CharField(max_length=1024)
    class Meta:
        table_name = "comment"


@snapshot.append
class CommentReplyModel(peewee.Model):
    author = snapshot.ForeignKeyField(backref='replies', index=True, model='usermodel')
    comment = snapshot.ForeignKeyField(backref='replies', index=True, model='commentmodel')
    content = CharField(max_length=256)
    class Meta:
        table_name = "comment_reply"


