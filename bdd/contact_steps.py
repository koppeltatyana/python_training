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
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')  # и это тоже фикстура
def verify_contact_added(db, contact_list, new_contact):
    old_contacts_list = contact_list
    new_contacts_list = db.get_contact_list()
    old_contacts_list += [new_contact]
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)


@given('non empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname"))
    return db.get_contact_list()


@given('a random contact from non empty contact list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')  # это тоже фикстура
def del_some_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without deleted contact')  # и это тоже фикстура
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts_list = non_empty_contact_list
    new_contacts_list = db.get_contact_list()
    old_contacts_list.remove(random_contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
