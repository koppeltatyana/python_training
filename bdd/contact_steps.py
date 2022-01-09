import random
from pytest_bdd import given, when, then  # пометки
from model.contact import Contact


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <middlename>, <lastname> and <address>')
def new_contact(firstname, middlename, lastname, address):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname, address=address)


@when('I add the contact to the list')  # это тоже фикстура
def add_new_group(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')  # и это тоже фикстура
def verify_group_added(db, contact_list, new_contact):
    old_contacts_list = contact_list
    new_contacts_list = db.get_contact_list()
    old_contacts_list += [new_contact]
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
