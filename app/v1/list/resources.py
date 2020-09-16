from flask_login import login_required
from flask_rebar import get_validated_body
from flask_rebar.errors import NotFound

from app.v1.list.models import ListModel


@login_required
def get_lists():
    return ListModel.select()


@login_required
def get_list_item(id):
    try:
        list_item = ListModel.get(id=id)
    except ListModel.DoesNotExist:
        raise NotFound
    except Exception as e:
        print(e)
    else:
        return list_item


@login_required
def create_list():
    data = get_validated_body()

    list = ListModel.create(**data)

    return list
