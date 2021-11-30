from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="John"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))  # случайным образом выбираем индекс удаляемого контакта
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
