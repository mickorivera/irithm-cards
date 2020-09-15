from flask import redirect
from flask_login import login_required, login_user, logout_user
from flask_rebar import get_validated_body

from app.v1.user.models import UserModel


def get_user_list():
    # TODO: return data from database
    return {
        "email": "micko@micko.com",
        "username": "micko",
        "password": "qwerty",
    }


def create_user():
    validated_body = get_validated_body()

    user = UserModel.create(
        username=validated_body.get("username"),
        email_address=validated_body.get("username"),
        password=validated_body.get("password"),
    )

    return user


def login():
    validated_body = get_validated_body()
    # TODO: compare user password
    user = UserModel.get(username=validated_body.get("username"))
    login_user(user=user)

    return user


@login_required
def logout():
    logout_user()

    return {}
