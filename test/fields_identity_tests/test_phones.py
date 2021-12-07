import re
from random import randrange


def test_phones_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear_number(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    assert merge_phones_like_on_home_page(contact_from_edit_page) == merge_phones_like_on_home_page(contact_from_view_page)


def clear_number(text):
    return re.sub("[() -+]", "", text)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # применяем фильтрацию к списку номеров (убираем пустые номера)
                            map(lambda x: clear_number(x),  # применяем функцию clear_number ко всем номерам
                                filter(lambda x: x is not None,  # применяем фиотрацию к списку номеров (убираем номера равные None)
                                       [contact.home_number, contact.mobile_number, contact.work_number, contact.phone2]))))
