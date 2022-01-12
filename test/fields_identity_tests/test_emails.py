from random import randrange
import allure


def test_emails_on_home_page(app):
    with allure.step("Given an  index for compering"):
        index = randrange(len(app.contact.get_contact_list()))
    with allure.step("Given contact's by index information from home page"):
        contact_from_home_page = app.contact.get_contact_list()[index]
    with allure.step("Given contact's by index information from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with allure.step("Then the contact's emails from home page is equal to the contact's emails from edit page"):
            assert merge_emails_like_on_home_page(contact_from_edit_page) == contact_from_home_page.all_emails_from_home_page


def test_emails_on_contact_view_page(app):
    with allure.step("Given an  index for compering"):
        index = randrange(len(app.contact.get_contact_list()))
    with allure.step("Given contact's by index information from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with allure.step("Given contact's by index information from view page"):
        contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    with allure.step("Then the contact's emails from edit page is equal to the contact's emails from view page"):
        assert merge_emails_like_on_home_page(contact_from_edit_page) == merge_emails_list_from_view_page(contact_from_view_page.all_emails_from_view_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))


def merge_emails_list_from_view_page(lst):
    return "\n".join(filter(lambda x: x != "", lst))
