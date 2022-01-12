from random import randrange
import allure
from model.contact import Contact


def test_first_last_names_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        with allure.step("If contact's list is empty, I'll create a new contact"):
            app.contact.create(Contact(firstname="NAME"))
    with allure.step("Given an  index for compering"):
        index = randrange(len(app.contact.get_contact_list()))
    with allure.step("Given contact's by index information from home page"):
        contact_from_home_page = app.contact.get_contact_list()[index]
    with allure.step("Given contact's by index information from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with allure.step("Then the contact's fullname from home page is equal to the contact's fullname from edit page"):
        assert merge_first_last_names_for_home_page(contact_from_home_page) == merge_first_last_names_for_home_page(contact_from_edit_page)


def test_first_last_names_on_view_page(app, db):
    if len(db.get_contact_list()) == 0:
        with allure.step("If contact's list is empty, I'll create a new contact"):
            app.contact.create(Contact(firstname="NAME"))
    with allure.step("Given an index for compering"):
        index = randrange(len(app.contact.get_contact_list()))
    with allure.step("Given contact's by index information from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with allure.step("Given contact's by index information from view page"):
        contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    with allure.step("Then the contact's fullname from edit page is equal to the contact's fullname from view page"):
        assert contact_from_view_page.fullname == merge_first_last_names_for_edit_page(contact_from_edit_page)


def merge_first_last_names_for_home_page(contact):  # соединяем фамилию и имя через пробел
    return " ".join(filter(lambda x: x != "", [contact.firstname, contact.lastname]))


def merge_first_last_names_for_edit_page(contact):  # соединяем фамилию, имя и отчество через пробел
    return " ".join(filter(lambda x: x != "", [contact.firstname, contact.middlename, contact.lastname]))
