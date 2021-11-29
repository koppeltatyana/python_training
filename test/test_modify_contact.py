from model.contact import Contact


def test_modify_first_contact(app):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="John"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='New First Name', lastname='New Last Name',
                      bday='13', aday='13', address='New Address')
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
