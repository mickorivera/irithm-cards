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
    print("========================")
    print(get_validated_body())
    print("========================")

    user = UserModel.create(
        username=validated_body.get("username"),
        email_address=validated_body.get("username"),
        password=validated_body.get("password"),
    )


    print("========================")

    print(user)
    print("========================")

    return user
