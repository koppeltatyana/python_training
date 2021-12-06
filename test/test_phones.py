import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear_number(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    assert merge_phones_like_on_home_page(contact_from_edit_page) == merge_phones_like_on_home_page(contact_from_view_page)


def clear_number(text):
    return re.sub("[() -+]", "", text)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # применяем фильтрацию к списку номеров (убираем пустые номера)
                            map(lambda x: clear_number(x),  # применяем функцию clear_number ко всем номерам
                                filter(lambda x: x is not None,  # применяем фиотрацию к списку номеров (убираем номера равные None)
                                       [contact.home_number, contact.mobile_number, contact.work_number, contact.phone2]))))
