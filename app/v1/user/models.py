from flask_login import UserMixin
from playhouse.postgres_ext import AutoField, CharField, DateTimeField

from app.common.models import BaseSQLModel


class UserModel(BaseSQLModel):
    id = AutoField()
    username = CharField(unique=True, index=True, max_length=16)
    email_address = CharField(unique=True, max_length=256)
    password = CharField(max_length=1024)
    date_updated = DateTimeField(null=True)

    class Meta(BaseSQLModel):
        table_name = "users"
