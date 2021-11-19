from model.group import Group


def test_modify_first_group(app):
    # вместо передачи параметров передаем объект класса Group
    app.group.modify_first_group(Group(group_name="New Name", group_header="New Header", group_footer="New Footer"))
    app.session.logout()
