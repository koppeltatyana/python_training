from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    # вместо передачи параметров передаем объект класса Group
    app.contact.modify_first_contact(Contact(first_name='Новый Томас', middle_name='Новый Джеффри', last_name='Новый Хэнкс', nickname='Новый Том', photo='', title='Новый Номер Томми', company='Новый Голливуд', address='Новый Лос-Анжелес', home_number='Новый 111222333', mobile_number='Новый +1465789159', work_number='Новый 789456123', fax='Новый 546546546', email='Новый thomas.hanks@gmail.com', email2='Новый tommi.king@gmail.com', email3='Новый tfhanks@yahoo.com', homepage='https://en.wikipedia.org/wiki/Tom_Hanks', bday='20', bmonth='December', byear='1995', aday='20', amonth='December', ayear='2025', address2='Новая Пляжная ул.', phone2='Новый 789456123', notes='SDFGHJKXCVBNMDFGHJ'))
    app.session.logout()
