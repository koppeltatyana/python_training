from model.group import Group


def test_delete_first_group(app):
    # добавление проверки: если ни одной группы не существует, то перед удалением создаем таковую
    if app.group.count_groups() == 0:
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
