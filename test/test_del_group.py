def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.delete_first_group()
    app.session.logout()
