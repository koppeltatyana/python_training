import random
import string
from model.contact import Contact

constant = [
    Contact(firstname='firstname1', middlename='middlename1', lastname='lastname1', nickname='nickname1', photo='',
            title='title1', company='company1', address='address1', home_number='111111', mobile_number='1111111',
            work_number='1111111', fax='1111111', email='mail@mail.ru', email2='mail2@mail.ru', email3='mail3@mail.ru',
            homepage='homepage', bday='10', bmonth='December', byear='1999', aday='10', amonth='December', ayear='2999',
            address2='address12', phone2='2222', notes='notes1'),
    Contact(firstname='firstname2', middlename='middlename2', lastname='lastname2', nickname='nickname2', photo='',
            title='title2', company='company2', address='address2', home_number='222222', mobile_number='33333',
            work_number='555555', fax='666666', email='mail21@mail.ru', email2='mail22@mail.ru', email3='mail23@mail.ru',
            homepage='homepage2', bday='10', bmonth='December', byear='1999', aday='10', amonth='December', ayear='2999',
            address2='address22', phone2='84848484', notes='notes2')
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_number(maxlen):
    symbols = '+' + string.digits + '-' * 5 + " " * 5
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_email(posfix, maxlen):
    symbols = string.ascii_letters + string.digits + "@" + "." * 2 + " " * 5
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen))) + posfix


def random_month():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', '-']
    return random.choice(months)


def random_day():
    days = ['-'] + [str(i) for i in range(1, 32)]
    return random.choice(days)


test_data = [Contact(firstname='', middlename='', lastname='', nickname='', photo='', title='',
                      company='', address='', home_number='', mobile_number='', work_number='',
                      fax='', email='', email2='', email3='', homepage='', bday='', bmonth='-',
                      byear='', aday='', amonth='-', ayear='', address2='', phone2='', notes='')] + \
            [
                Contact(firstname=random_string('f', 5), middlename=random_string('m', 5), lastname=random_string('l', 5),
                        nickname=random_string('n', 5), photo='', title=random_string('title', 10), company=random_string('comp', 5),
                        address=random_string('address', 25), home_number=random_number(10), mobile_number=random_number(10), work_number=random_number(10),
                        fax=random_number(10), email=random_email(".com", 20), email2=random_email(".ru", 20), email3=random_email(".com", 20),
                        homepage=random_string("homepage", 5), bday=random_day(), bmonth=random_month(),
                        byear=random.randint(1900, 2050), aday=random_day(), amonth=random_month(), ayear=random.randint(1900, 2050),
                        address2=random_string("address2", 50), phone2=random_number(10), notes=random_string("address2", 150))
                for i in range(8)
]