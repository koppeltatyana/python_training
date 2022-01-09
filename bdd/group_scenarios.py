# пишем запускатель для сценариев
from pytest_bdd import scenario
from .group_steps import *  # импортируем шаги, чтобы сценарий имел доступ к шагам


@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete some group')
def test_del_some_group():
    pass


@scenario('groups.feature', 'Modify some group')
def test_del_some_group():
    pass
