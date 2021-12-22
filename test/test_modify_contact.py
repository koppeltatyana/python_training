from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="John"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    new_contact = Contact(firstname='New First Name', lastname='New Last Name', address='New Address')
    app.contact.modify_contact_by_id(random_contact.id, new_contact)

    res_old_contacts = []
    for i in range(len(old_contacts)):
        if str(old_contacts[i].id) != str(random_contact.id):
            res_old_contacts += [old_contacts[i]]
        if str(old_contacts[i].id) == str(random_contact.id):
            res_old_contacts += [new_contact]
    new_contacts = db.get_contact_list()
    assert res_old_contacts == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
