def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_contact_firstname(new_firstname='Новое имя контакта')
    app.session.logout()


def test_modify_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_contact_middlename(new_middlename='Новое отчество контакта')
    app.session.logout()


def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_contact_lastname(new_lastname='Новая фамилия контакта')
    app.session.logout()


def test_modify_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_contact_nickname(new_nickname='Новая фамилия контакта')
    app.session.logout()
