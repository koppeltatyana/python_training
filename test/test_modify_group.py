from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group(Group(name="New Name", header="New Header", footer="New Footer"))
    app.session.logout()
