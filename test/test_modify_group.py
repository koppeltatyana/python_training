def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group(new_group_name="New Name")
    app.session.logout()
