import allure
from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="John"))
    with allure.step("Given non empty contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("Given a random contact from non empty contact list"):
        contact = random.choice(old_contacts)
    with allure.step("When I delete the contact {} from the list".format(contact)):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step("Then the new contact list is equal to the old contact list without deleted contact"):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
