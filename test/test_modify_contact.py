from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    # передаем только те параметры, которые хотим изменить, добавив 'new' к названию переменной
    app.contact.modify_first_contact(Contact(firstname='asd', lastname='qweqwe', bday='12', aday='12'))
    app.session.logout()
