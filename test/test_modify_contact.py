def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_firstname(new_firstname='Новое имя контакта')
    app.session.logout()


def test_modify_first_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_middlename(new_middlename='Новое отчество контакта')
    app.session.logout()


def test_modify_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_lastname(new_lastname='Новая фамилия контакта')
    app.session.logout()


def test_modify_first_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_nickname(new_nickname='Новая фамилия контакта')
    app.session.logout()


def test_modify_first_contact_title(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_title(new_title='Новая фамилия контакта')
    app.session.logout()


def test_modify_first_contact_company(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_company(new_company='Новая фамилия контакта')
    app.session.logout()


def test_modify_first_contact_address(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_address(new_address='Новая фамилия контакта')
    app.session.logout()
