from model.contact import Contact


def test_modify_first_contact(app):
    # передаем только те параметры, которые хотим изменить, добавив 'new' к названию переменной
    app.contact.modify_first_contact(Contact(firstname='New First Name', lastname='New Last Name', bday='13', aday='13', address='New Address'))
    app.session.logout()
