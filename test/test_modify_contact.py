from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact(Contact(first_name='Новый Томас', middle_name='Новый Джеффри', last_name='Новый Хэнкс', nickname='Новый Том', photo='', title='Новый Номер Томми', company='Новый Голливуд', address='Новый Лос-Анжелес', home_number='Новый 111222333', mobile_number='Новый +1465789159', work_number='Новый 789456123', fax='Новый 546546546', email='Новый thomas.hanks@gmail.com', email2='Новый tommi.king@gmail.com', email3='Новый tfhanks@yahoo.com', homepage='https://en.wikipedia.org/wiki/Tom_Hanks', bday='20', bmonth='December', byear='1995', aday='20', amonth='December', ayear='2025', address2='Новая Пляжная ул.', phone2='Новый 789456123', notes='SDFGHJKXCVBNMDFGHJ'))
    app.session.logout()


def test_modify_first_contact_firstname(app):
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


def test_modify_first_contact_bday(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_bday(new_bday='20', new_bmonth='December', new_byear='1995')
    app.session.logout()


def test_modify_first_contact_aday(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_aday(new_aday='20', new_amonth='December', new_ayear='2025')
    app.session.logout()


def test_modify_first_contact_address2(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_address2(new_address2='New address2')
    app.session.logout()


def test_modify_first_contact_phone2(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_phone2(new_phone2='New phone2')
    app.session.logout()


def test_modify_first_contact_notes(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact_notes(new_notes='New notes')
    app.session.logout()
