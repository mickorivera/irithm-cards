from http import HTTPStatus

from app import RestApp
from app.utils.time import format_date
from app.v1.user.models import UserModel


class TestListIndex:
    def setup_method(self):
        app = RestApp()

        @app.login_manager.user_loader
        def load_user(user_id):
            try:
                user = UserModel.get(user_id)
            except UserModel.DoesNotExist:
                return None
            else:
                return user

        self._app_client = app.test_client()

        self.content_type = "application/json"
        self.endpoint = "v1/lists"

    def test_get_lists(self, lists):
        self._app_client.post(
            "v1/login",
            content_type=self.content_type,
            json={
                "username": "user1",
                "password": "password1",
            },
        )

        response = self._app_client.get(
            self.endpoint,
            content_type=self.content_type,
        )

        assert HTTPStatus.OK == response.status_code
        expected_response = [
            {
                "id": app_list.id,
                "author_id": app_list.author_id,
                "title": app_list.title,
                "date_created": format_date(app_list.date_created),
                "date_updated": format_date(app_list.date_updated),
            }
            for app_list in lists
        ]
        assert expected_response == response.json

    def test_get_lists_unauthorized(self, lists):
        response = self._app_client.get(
            self.endpoint,
            content_type=self.content_type,
        )

        assert HTTPStatus.UNAUTHORIZED == response.status_code
        assert {"message": "Unauthorized"} == response.json


class TestListShow:
    def setup_method(self):
        app = RestApp()

        @app.login_manager.user_loader
        def load_user(user_id):
            try:
                user = UserModel.get(user_id)
            except UserModel.DoesNotExist:
                return None
            else:
                return user

        self._app_client = app.test_client()

        self.content_type = "application/json"
        self.endpoint = "v1/lists/{id}"

    def test_get_list(self, lists):
        self._app_client.post(
            "v1/login",
            content_type=self.content_type,
            json={
                "username": "user1",
                "password": "password1",
            },
        )

        response = self._app_client.get(
            self.endpoint.format(id=lists[0].id),
            content_type=self.content_type,
        )

        assert HTTPStatus.OK == response.status_code
        expected_response = {
            "id": lists[0].id,
            "author_id": lists[0].author_id,
            "title": lists[0].title,
            "date_created": format_date(lists[0].date_created),
            "date_updated": format_date(lists[0].date_updated),
        }
        assert expected_response == response.json

    def test_get_list_not_found(self, lists):
        self._app_client.post(
            "v1/login",
            content_type=self.content_type,
            json={
                "username": "user1",
                "password": "password1",
            },
        )

        response = self._app_client.get(
            self.endpoint.format(id=-1),
            content_type=self.content_type,
        )

        assert HTTPStatus.NOT_FOUND == response.status_code
        assert {"message": "Not Found"} == response.json

    def test_get_list_unauthorized(self, lists):
        response = self._app_client.get(
            self.endpoint.format(id=lists[0].id),
            content_type=self.content_type,
        )

        assert HTTPStatus.UNAUTHORIZED == response.status_code
        assert {"message": "Unauthorized"} == response.json
