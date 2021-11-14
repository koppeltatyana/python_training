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
    app.contact.modify_first_contact_nickname(new_nickname='Новый ник контакта')
    app.session.logout()


def test_modify_first_contact_title(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_title(new_title='Новая титульная информация контакта')
    app.session.logout()


def test_modify_first_contact_company(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_company(new_company='Новая компания контакта')
    app.session.logout()


def test_modify_first_contact_address(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_address(new_address='Новый адрес контакта')
    app.session.logout()


def test_modify_first_contact_home_number(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_home_number(new_home_number='11112222333')
    app.session.logout()


def test_modify_first_contact_mobile_number(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_mobile_number(new_mobile_number='2222333344455')
    app.session.logout()


def test_modify_first_contact_work_number(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_work_number(new_work_number='333444555666')
    app.session.logout()


def test_modify_first_contact_fax(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_fax(new_fax='444555666777')
    app.session.logout()


def test_modify_first_contact_email(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_email(new_email='qwe@qwe.qwe')
    app.session.logout()


def test_modify_first_contact_email2(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_email2(new_email2='asd@asd.asd')
    app.session.logout()


def test_modify_first_contact_email3(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_email3(new_email3='zxc@zxc.zxc')
    app.session.logout()


def test_modify_first_contact_homepage(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_homepage(new_homepage='New homepage')
    app.session.logout()
