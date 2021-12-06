import re


def test_first_last_names_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert merge_first_last_names_for_home_page(contact_from_home_page) == merge_first_last_names_for_home_page(contact_from_edit_page)


def test_first_last_names_on_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    assert contact_from_view_page.fullname == merge_first_last_names_for_edit_page(contact_from_edit_page)


def merge_first_last_names_for_home_page(contact):  # соединяем фамилию и имя через пробел
    return " ".join(filter(lambda x: x != "", [contact.firstname, contact.lastname]))


def merge_first_last_names_for_edit_page(contact):  # соединяем фамилию, имя и отчество через пробел
    return " ".join(filter(lambda x: x != "", [contact.firstname, contact.middlename, contact.lastname]))
