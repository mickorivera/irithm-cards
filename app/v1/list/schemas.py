from marshmallow import fields, Schema


class ListSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    author_id = fields.Integer()
    date_created = fields.String(dump_only=True)
    date_updated = fields.String(dump_only=True)
