from random import randrange
import allure


def test_address_on_home_page(app):
    with allure.step("Given an  index for compering"):
        index = randrange(len(app.contact.get_contact_list()))
    with allure.step("Given contact's by index information from home page"):
        contact_from_home_page = app.contact.get_contact_list()[index]
    with allure.step("Given contact's by index information from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with allure.step("Then the contact's address from home page is equal to the contact's address from edit page"):
        assert contact_from_home_page.address == contact_from_edit_page.address
