import os
import pytest
from http import HTTPStatus

from app import RestApp
from app.utils.hashing import get_hash
from app.v1.user.models import UserModel


class TestUserLogin:
    def setup_method(self):
        self._app = RestApp().test_client()

        self.endpoint = "v1/login"
        self.content_type = "application/json"

    @pytest.fixture(scope="class", autouse=True)
    def seed_event_tables(self):
        if UserModel.table_exists():
            UserModel.drop_table(cascade=True)

        UserModel.create_table()

        salt = os.urandom(32)
        UserModel.create(
            username="user1",
            email_address="user1@gmail.com",
            key=get_hash(password="password1", salt=salt),
            salt=salt,
        )
        UserModel.create(
            username="user2",
            email_address="user2@gmail.com",
            key=get_hash(password="password2", salt=salt),
            salt=salt,
        )
        yield
        UserModel.truncate_table(cascade=True)

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {
                    "username": "user1",
                    "password": "password1",
                },
                {
                    "status_code": HTTPStatus.OK,
                    "response": {"username": "user1"},
                },
            ),
            (
                {
                    "username": "user1",
                    "password": "incorrectpassword",
                },
                {
                    "status_code": HTTPStatus.UNAUTHORIZED,
                    "response": {"message": "Unauthorized"},
                },
            ),
            (
                {
                    "username": "incorrectusername",
                    "password": "password1",
                },
                {
                    "status_code": HTTPStatus.NOT_FOUND,
                    "response": {"message": "Not Found"},
                },
            ),
        ],
    )
    def test_login(self, test_input, expected):
        response = self._app.post(
            self.endpoint,
            content_type=self.content_type,
            json=test_input,
        )

        assert expected["status_code"] == response.status_code
        assert expected["response"] == response.json


class TestUserLogout:
    def setup_method(self):
        self._app = RestApp().test_client()

        self.endpoint = "v1/logout"
        self.content_type = "application/json"

    @pytest.fixture(scope="class", autouse=True)
    def seed_event_tables(self):
        if UserModel.table_exists():
            UserModel.drop_table(cascade=True)

        UserModel.create_table()

        salt = os.urandom(32)
        UserModel.create(
            username="user1",
            email_address="user1@gmail.com",
            key=get_hash(password="password1", salt=salt),
            salt=salt,
        )
        yield
        UserModel.truncate_table(cascade=True)
