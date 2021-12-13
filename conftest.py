import pytest
import json
import os.path
from fixture.application import Application
import importlib
import data

fixture = None
target = None


@pytest.fixture
def app(request):  # функция, инициализирующая фикстуру
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        # сначала берем абсолютный путь от файла __file__ (это у нас файл conftest)
        # далее берем название дииректории, в котором нах-ся conftest
        # к директории приклеиваем значение из "--target", которое по дефолту == target.json
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])  # создание фикстуры

    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")  # храним все остальные параметры в файле


def pytest_generate_tests(metafunc):  # функция для генерации тестов
    for fixture in metafunc.fixturenames:  # пробегаем по всем параметрам
        print(fixture[5:])

        if fixture.startswith("data_"):
            test_data = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_form_module(module):  # берет из модуля данные
    return importlib.import_module("data.{0}".format(module)).test_data
