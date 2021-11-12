# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):  # функция, инициализирующая фикстуру
    fixture = Application()  # создание фикстуры
    request.addfinalizer(fixture.destroy)  # метод, который показывает, как фикстура должна быть разрушена
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name='Томас', middle_name='Джеффри', last_name='Хэнкс', nickname='Том', photo='', title='Номер Томми', company='Голливуд', address='Лос-Анжелес', home_number='111222333', mobile_number='+1465789159', work_number='789456123', fax='546546546', email='thomas.hanks@gmail.com', email2='tommi.king@gmail.com', email3='tfhanks@yahoo.com', homepage='https://en.wikipedia.org/wiki/Tom_Hanks', bday='10', bmonth='October', byear='1965', aday='10', amonth='October', ayear='2025', address2='Пляжная ул.', phone2='789456123', notes='Qweashgdfaghcxhgzctafsd'))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name='', middle_name='', last_name='', nickname='', photo='', title='', company='', address='', home_number='', mobile_number='', work_number='', fax='', email='', email2='', email3='', homepage='', bday='', bmonth='-', byear='', aday='', amonth='-', ayear='', address2='', phone2='', notes=''))
    app.logout()
