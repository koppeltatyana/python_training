def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.delete_first_contact()
    app.session.logout()
