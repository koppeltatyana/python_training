from model.contact import Contact


def test_modify_first_contact(app):
    # добавление проверки: если нет ни одного контакта, то перед удалением создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John"))
    app.contact.modify_first_contact(Contact(firstname='New First Name', lastname='New Last Name', bday='13', aday='13', address='New Address'))
