from model.contact import Contact
import random


def test_modify_some_contact(app, db):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="John"))

    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    new_contact = Contact(firstname='New First Name', lastname='New Last Name',
                      bday='13', aday='13', address='New Address')
    app.contact.modify_contact_by_id(random_contact.id, new_contact)
    new_contacts = db.get_contact_list()
    for contact in old_contacts:  # чтобы проверить соответствие списков, заменяем элемент с нужным id в старом списке на новый элемент
        if contact.id == random_contact.id:
            contact = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
