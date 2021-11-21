import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app():  # функция, инициализирующая фикстуру
    global fixture

    if fixture is None:
        fixture = Application()  # создание фикстуры
    else:
        if not fixture.is_valid():
            fixture = Application()  # создание фикстуры
            fixture.session.login(username='admin', password='secret')
    fixture.session.ensure_login(username='admin', password='secret')
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
