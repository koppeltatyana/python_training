import allure
from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="John"))
    with allure.step("Given non empty contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("Given a random contact from non empty contact list"):
        random_contact = random.choice(old_contacts)
    with allure.step("Given a new contact"):
        new_contact = Contact(firstname='New First Name', lastname='New Last Name', address='New Address')
    with allure.step("When I modify the contact '{}' from the list".format(random_contact)):
        app.contact.modify_contact_by_id(random_contact.id, new_contact)
    with allure.step("Then the new contact list is equal to the old contact list with modify contact"):
        old_contacts[old_contacts.index(random_contact)] = new_contact
        new_contacts = db.get_contact_list()
        assert old_contacts == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
