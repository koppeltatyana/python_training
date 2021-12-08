from random import randrange


def test_emails_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert merge_emails_like_on_home_page(contact_from_edit_page) == contact_from_home_page.all_emails_from_home_page


def test_emails_on_contact_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    assert merge_emails_like_on_home_page(contact_from_edit_page) == merge_emails_list_from_view_page(contact_from_view_page.all_emails_from_view_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))


def merge_emails_list_from_view_page(lst):
    return "\n".join(filter(lambda x: x != "", lst))
