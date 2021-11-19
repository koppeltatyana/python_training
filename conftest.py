import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):  # функция, инициализирующая фикстуру
    fixture = Application()  # создание фикстуры
    fixture.session.login(username='admin', password='secret')

    # метод, который делает разлогин и разрушает фикстуру после тестов
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
