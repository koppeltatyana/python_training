import allure

from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    with allure.step("Given a ui_list of groups"):
        ui_list = app.group.get_group_list()

    def clean(group):  # убираем наши лишние пробелы (только в нашем тесте)
        return Group(group_id=group.id, group_name=group.group_name.strip())

    with allure.step("Given a db_list of groups"):
        db_list = map(clean, db.get_group_list())
    with allure.step("Then the group's list from ui is equal to the group's list from db"):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    with allure.step("Given a ui_list of contacts"):
        ui_list = app.contact.get_contact_list()

    def clean(contact):  # убираем наши лишние пробелы (только в нашем тесте)
        return Contact(contact_id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    with allure.step("Given a db_list of contacts"):
        db_list = list(map(clean, db.get_contact_list()))
    with allure.step("Then the contact's list from ui is equal to the contact's list from db"):
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
