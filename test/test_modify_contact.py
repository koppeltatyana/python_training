def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    # передаем только те параметры, которые хотим изменить, добавив 'new' к названию переменной
    app.contact.modify_first_contact(new_firstname='asd', new_lastname='qweqwe', new_bday='12', new_aday='12')
    app.session.logout()
