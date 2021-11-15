def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact(new_firstname='asd')
    app.session.logout()
