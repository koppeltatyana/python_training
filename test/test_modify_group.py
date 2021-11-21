from model.group import Group


def test_modify_first_group(app):
    # добавление проверки: если ни одной группы не существует, то перед удалением создаем таковую
    if app.group.count() == 0:
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    app.group.modify_first_group(Group(group_name="New Name", group_header="New Header", group_footer="New Footer"))
