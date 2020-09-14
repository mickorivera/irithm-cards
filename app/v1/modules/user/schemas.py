from marshmallow import fields, Schema


class UserSchema(Schema):
    # TODO: secure password
    # TODO: validate email/username
    email = fields.Email()
    username = fields.String()
    password = fields.String(load_only=True)
