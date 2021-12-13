# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import constant as test_data


@pytest.mark.parametrize("contact", test_data, ids=[repr(cntct) for cntct in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()  # функция count_groups используется как хэш
    new_contacts = app.contact.get_contact_list()
    old_contacts += [contact]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
