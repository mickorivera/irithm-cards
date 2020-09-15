from marshmallow import fields, Schema


class ListSchema(Schema):
    title = fields.String()
