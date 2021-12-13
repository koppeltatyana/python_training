# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.add_group import constant as test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(gr) for gr in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    # вместо передачи параметров передаем объект класса Group
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_groups()  # функция count_groups используется как хэш
    new_groups = app.group.get_group_list()
    old_groups += [group]
    # теперь сравниваем отсортированные списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
