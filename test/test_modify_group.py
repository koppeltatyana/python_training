from model.group import Group


def test_modify_first_group(app):
    # добавление проверки: если ни одной группы не существует, то перед удалением создаем таковую
    if app.group.count_groups() == 0:
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    old_groups = app.group.get_group_list()
    group = Group(group_name="New Name", group_header="New Header", group_footer="New Footer")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    # теперь сравниваем отсортированные списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
