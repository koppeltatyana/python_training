from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="John"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))  # случайным образом выбираем индекс удаляемой группы
    contact = Contact(firstname='New First Name', lastname='New Last Name',
                      bday='13', aday='13', address='New Address')
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
