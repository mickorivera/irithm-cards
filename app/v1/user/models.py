from playhouse.postgres_ext import CharField

from app.common.models import BaseSQLModel


class UserModel(BaseSQLModel):
    username = CharField(primary_key=True, index=True, max_length=16)
    email_address = CharField(unique=True, max_length=256)
    password = CharField(max_length=1024)

    class Meta(BaseSQLModel):
        table_name = "user"
