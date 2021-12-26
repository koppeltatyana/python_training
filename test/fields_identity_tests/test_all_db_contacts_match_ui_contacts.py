from model.contact import Contact
from fixture.db import DbFixture
import re

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_all_db_contacts_match_ui_contacts(app):
    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    # первоначальная проверка длин списков контактов с ui и db
    assert len(contacts_from_db) == len(contacts_from_ui)

    for i in range(len(contacts_from_ui)):
        # проверка соответствия имен
        ui_contact_full_name = merge_first_last_names(contacts_from_ui[i])
        db_contact_full_name = merge_first_last_names(contacts_from_db[i])
        assert ui_contact_full_name == db_contact_full_name

        # проверка соответствия электронных адресов
        db_contact_emails = merge_emails_like_on_home_page(contacts_from_db[i])
        assert db_contact_emails == contacts_from_ui[i].all_emails_from_home_page

        # проверка соответствия телефонов
        db_contact_phones = clear_number(merge_phones_like_on_home_page(contacts_from_db[i]))
        assert db_contact_phones == contacts_from_ui[i].all_phones_from_home_page

        # проверка соответствия адресов
        assert clear_double_spaces(contacts_from_db[i].address) == clear_double_spaces(contacts_from_ui[i].address)


def clear_number(text):
    return re.sub("[() *-]", "", text)


def clear_double_spaces(text):
    return " ".join(text.split())


def merge_first_last_names(contact):  # соединяем фамилию и имя через пробел
    return " ".join(filter(lambda x: x != "", [contact.firstname.strip(), contact.lastname.strip()]))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # применяем фильтрацию к списку номеров (убираем пустые номера)
                            map(lambda x: clear_number(x),  # применяем функцию clear_number ко всем номерам
                                filter(lambda x: x is not None,  # применяем фиотрацию к списку номеров (убираем номера равные None)
                                       [contact.home_number, contact.mobile_number, contact.work_number, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))
