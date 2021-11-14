def test_modify_name_group(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group_name(new_name='Новое имя группы')
    app.session.logout()


def test_modify_header_group(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group_header(new_header='Новое Лого')
    app.session.logout()


def test_modify_footer_group(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group_footer(new_footer='Новый комментарий')
    app.session.logout()
