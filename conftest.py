import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):  # функция, инициализирующая фикстуру
    fixture = Application()  # создание фикстуры
    request.addfinalizer(fixture.destroy)  # метод, который показывает, как фикстура должна быть разрушена
    return fixture
