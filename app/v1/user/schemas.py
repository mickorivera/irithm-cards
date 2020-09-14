from marshmallow import fields, Schema


class UserSchema(Schema):
    # TODO: secure password
    # TODO: validate email/username
    email_address = fields.String()
    username = fields.String()
    password = fields.String(load_only=True)
    date_created = fields.String(dump_only=True)

