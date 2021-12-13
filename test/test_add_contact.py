# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()  # функция count_groups используется как хэш
    new_contacts = app.contact.get_contact_list()
    old_contacts += [contact]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
