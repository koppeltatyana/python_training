# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # вместо передачи параметров передаем объект класса Group
    app.group.create(Group(group_name="asd", group_header="asd", group_footer="asd"))


def test_add_empty_group(app):
    app.group.create(Group(group_name="", group_header="", group_footer=""))
