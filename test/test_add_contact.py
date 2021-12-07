# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_number(maxlen):
    symbols = '+' + string.digits + '-' * 5 + " " * 5
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_email(posfix, maxlen):
    symbols = string.ascii_letters + string.digits + "@" + "." * 2 + " " * 5
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen))) + posfix


def random_month():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', '-']
    return random.choice(months)


def random_day():
    days = ['-'] + [str(i) for i in range(1, 32)]
    return random.choice(days)


test_data = [Contact(firstname='', middlename='', lastname='', nickname='', photo='', title='',
                      company='', address='', home_number='', mobile_number='', work_number='',
                      fax='', email='', email2='', email3='', homepage='', bday='', bmonth='-',
                      byear='', aday='', amonth='-', ayear='', address2='', phone2='', notes='')] + \
            [
                Contact(firstname=random_string('f', 5), middlename=random_string('m', 5), lastname=random_string('l', 5),
                        nickname=random_string('n', 5), photo='', title=random_string('title', 10), company=random_string('comp', 5),
                        address=random_string('address', 25), home_number=random_number(10), mobile_number=random_number(10), work_number=random_number(10),
                        fax=random_number(10), email=random_email(".com", 20), email2=random_email(".ru", 20), email3=random_email(".com", 20),
                        homepage=random_string("homepage", 5), bday=random_day(), bmonth=random_month(),
                        byear=random.randint(1900, 2050), aday=random_day(), amonth=random_month(), ayear=random.randint(1900, 2050),
                        address2=random_string("address2", 50), phone2=random_number(10), notes=random_string("address2", 150))
                for i in range(8)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(cntct) for cntct in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()  # функция count_groups используется как хэш
    new_contacts = app.contact.get_contact_list()
    old_contacts += [contact]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
