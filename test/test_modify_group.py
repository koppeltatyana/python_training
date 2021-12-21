from model.group import Group
from random import randrange
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
    for group in old_groups:
        if group.id == random_group.id:
            group = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
