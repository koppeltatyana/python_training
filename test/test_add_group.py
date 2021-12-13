# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    # вместо передачи параметров передаем объект класса Group
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_groups()  # функция count_groups используется как хэш
    new_groups = app.group.get_group_list()
    old_groups += [group]
    # теперь сравниваем отсортированные списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
