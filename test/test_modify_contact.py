def test_modify_name_contact(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_contact_firstname(new_firstname='Новое имя контакта')
    app.session.logout()
