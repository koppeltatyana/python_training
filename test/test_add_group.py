# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):  # функция, инициализирующая фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)  # некий деструктор фикстуры
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.group.create(Group(name="asd", header="asd", footer="asd"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
