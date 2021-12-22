from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    # добавление проверки: если ни одной группы не существует, то перед удалением создаем таковую
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)  # случайным образом выбираем группe для модификации
    new_group = Group(group_name="New Name", group_header="New Header", group_footer="New Footer")
    app.group.modify_group_by_id(random_group.id, new_group)
    new_groups = db.get_group_list()
    res_old_groups = []
    for i in range(len(old_groups)):
        if str(old_groups[i].id) != str(random_group.id):
            res_old_groups += [old_groups[i]]
        if str(old_groups[i].id) == str(random_group.id):
            res_old_groups += [new_group]
    assert res_old_groups == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
