from flask_rebar import SwaggerV3Generator
from flask_rebar.rebar import HandlerRegistry

from app.v1.modules.card.resources import get_card_list
from app.v1.modules.card.schemas import CardSchema
from app.v1.modules.comment.resources import (
    get_all_comments,
    get_comment_replies,
)
from app.v1.modules.comment.schemas import CommentReplySchema, CommentSchema
from app.v1.modules.list.resources import get_lists
from app.v1.modules.list.schemas import ListSchema
from app.v1.modules.user.resources import get_user_list
from app.v1.modules.user.schemas import UserSchema
from config import get_config


swagger_generator = SwaggerV3Generator(
    version="1.0.0",
    title="Irithm API V1",
    description="Sample API for Irithm Application",
)

config = get_config()
version_1_registry = HandlerRegistry(
    default_mimetype="application/json",
    prefix="/v1",
    swagger_generator=swagger_generator,
    swagger_path="/swagger" if config.DEBUG else None,
    swagger_ui_path="/swagger/ui" if config.DEBUG else None,
)

# Cards Endpoints
version_1_registry.add_handler(
    get_card_list,
    rule="/cards",
    method="GET",
    response_body_schema=CardSchema(),
)

# Comment Endpoints
version_1_registry.add_handler(
    get_all_comments,
    rule="/comments",
    method="GET",
    response_body_schema=CommentSchema(),
)

version_1_registry.add_handler(
    get_comment_replies,
    rule="/comment-replies",
    method="GET",
    response_body_schema=CommentReplySchema(),
)

# List Endpoints
version_1_registry.add_handler(
    get_lists,
    rule="/lists",
    method="GET",
    response_body_schema=ListSchema(),
)

# User Endpoints
version_1_registry.add_handler(
    get_user_list,
    rule="/users",
    method="GET",
    response_body_schema=UserSchema(),
)
