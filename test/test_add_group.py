# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


test_data = [Group(group_name="", group_header="", group_footer="")] + [
        Group(group_name=random_string('name', 5), group_header=random_string('header', 10), group_footer=random_string('footer', 20))
        for i in range(8)
    ]
# [
#     Group(group_name=name, group_header=random_string('header', 10), group_footer=random_string('footer', 20))
#     for name in ["", random_string('name', 5)]
#     for header in ["", random_string('header', 15)]
#     for footer in ["", random_string('footer', 25)]
# ]


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
