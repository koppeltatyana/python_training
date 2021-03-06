# -*- coding: utf-8 -*-
import allure
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()  # сделали чтобы список старых групп читался из БД, а не из ui
    # вместо передачи параметров передаем объект класса Group
    with allure.step("When I add a group '{}' to the list".format(group)):
        app.group.create(group)
    with allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()  # сделали чтобы список новых групп читался из БД, а не из ui
        old_groups += [group]
        # теперь сравниваем отсортированные списки групп
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
