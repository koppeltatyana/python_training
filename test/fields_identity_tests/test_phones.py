import re
from random import randrange
import allure
from model.contact import Contact


def test_phones_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        with allure.step("If contact's list is empty, I'll create a new contact"):
            app.contact.create(Contact(firstname="NAME"))
    with allure.step("Given an  index for compering"):
        index = randrange(len(app.contact.get_contact_list()))
    with allure.step("Given contact's by index information from home page"):
        contact_from_home_page = app.contact.get_contact_list()[index]
    with allure.step("Given contact's by index information from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with allure.step("Then the contact's phones from home page is equal to the contact's phones from edit page"):
        assert clear_number(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app, db):
    if len(db.get_contact_list()) == 0:
        with allure.step("If contact's list is empty, I'll create a new contact"):
            app.contact.create(Contact(firstname="NAME"))
    with allure.step("Given an  index for compering"):
        index = randrange(len(app.contact.get_contact_list()))
    with allure.step("Given contact's by index information from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with allure.step("Given contact's by index information from view page"):
        contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    with allure.step("Then the contact's phones from edit page is equal to the contact's phones from view page"):
        assert merge_phones_like_on_home_page(contact_from_edit_page) == merge_phones_like_on_home_page(contact_from_view_page)


def clear_number(text):
    return re.sub("[() *+-]", "", text)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # применяем фильтрацию к списку номеров (убираем пустые номера)
                            map(lambda x: clear_number(x),  # применяем функцию clear_number ко всем номерам
                                filter(lambda x: x is not None,  # применяем фиотрацию к списку номеров (убираем номера равные None)
                                       [contact.home_number, contact.mobile_number, contact.work_number, contact.phone2]))))
