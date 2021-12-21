# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_group_list()  # сделали чтобы список старых групп читался из БД, а не из ui
    # вместо передачи параметров передаем объект класса Group
    app.group.create(group)
    new_groups = db.get_group_list()  # сделали чтобы список новых групп читался из БД, а не из ui
    old_groups += [group]
    # теперь сравниваем отсортированные списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
