from model.contact import Contact
import random


def test_delete_some_contact(app, db):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="John"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
