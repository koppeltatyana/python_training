def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group_name(new_name='Новое имя группы')
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group_header(new_header='Новое Лого')
    app.session.logout()


def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group_footer(new_footer='Новый комментарий')
    app.session.logout()