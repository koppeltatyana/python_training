# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    # вместо передачи параметров передаем объект класса Group
    group = Group(group_name="asd", group_header="asd", group_footer="asd")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups += [group]
    # теперь сравниваем отсортированные списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="", group_header="", group_footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups += [group]
    # теперь сравниваем отсортированные списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
