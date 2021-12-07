from random import randrange


def test_first_last_names_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert merge_first_last_names_for_home_page(contact_from_home_page) == merge_first_last_names_for_home_page(contact_from_edit_page)


def test_first_last_names_on_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    assert contact_from_view_page.fullname == merge_first_last_names_for_edit_page(contact_from_edit_page)


def merge_first_last_names_for_home_page(contact):  # соединяем фамилию и имя через пробел
    return " ".join(filter(lambda x: x != "", [contact.firstname, contact.lastname]))


def merge_first_last_names_for_edit_page(contact):  # соединяем фамилию, имя и отчество через пробел
    return " ".join(filter(lambda x: x != "", [contact.firstname, contact.middlename, contact.lastname]))
