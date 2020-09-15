from marshmallow import fields, Schema, validate

from app.constants import UserRole


class UserSchema(Schema):
    # TODO: secure password
    # TODO: validate email/username
    email_address = fields.String()
    username = fields.String()
    password = fields.String(load_only=True)
    date_created = fields.String(dump_only=True)
    user_role = fields.String(
        default=UserRole.MEMBER, validate=validate.OneOf(UserRole)
    )
