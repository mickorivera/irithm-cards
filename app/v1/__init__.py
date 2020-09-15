from flask_rebar import HeaderApiKeyAuthenticator, SwaggerV3Generator
from flask_rebar.rebar import HandlerRegistry

from app.v1.card.resources import get_card_list
from app.v1.card.schemas import CardSchema
from app.v1.comment.resources import (
    get_all_comments,
    get_comment_replies,
)
from app.v1.comment.schemas import CommentReplySchema, CommentSchema
from app.v1.list.resources import get_lists
from app.v1.list.schemas import ListSchema
from app.v1.user.resources import create_user, get_user_list, login, logout
from app.v1.user.schemas import UserSchema
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
# TODO: enable auth
# authenticator = HeaderApiKeyAuthenticator(header='X-MyApp-ApiKey')
# authenticator.register_key(key='my-secret-api-key')

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

version_1_registry.add_handler(
    create_user,
    rule="/sign-up",
    method="POST",
    request_body_schema=UserSchema(),
    response_body_schema=UserSchema(),
)

version_1_registry.add_handler(
    login,
    rule="/login",
    method="POST",
    request_body_schema=UserSchema(),
    response_body_schema=UserSchema(),
)

version_1_registry.add_handler(
    logout,
    rule="/logout",
    method="POST",
    response_body_schema=UserSchema(),
)
