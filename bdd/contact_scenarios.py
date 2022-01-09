# пишем запускатель для сценариев
from pytest_bdd import scenario
from .contact_steps import *  # импортируем шаги, чтобы сценарий имел доступ к шагам


@scenario('contacts.feature', 'Add new contact')
def test_add_new_contact():
    pass


@scenario('contacts.feature', 'Delete some contact')
def test_del_some_contact():
    pass
