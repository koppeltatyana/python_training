from random import randrange


def test_address_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address


# def test_address_on_view_page(app):
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
#     # print(contact_from_edit_page.address, contact_from_edit_page.address2, sep="**********", end='\n\n\n\n\n')
