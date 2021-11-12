# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request): # функция, инициализирующая фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy()) # некий деструктор фикстуры
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="asd", header="asd", footer="asd")) # вместо передачи параметров передаем объект класса Group
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
