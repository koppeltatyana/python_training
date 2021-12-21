import getopt
import random
import string
import sys
from model.contact import Contact
import os.path
import jsonpickle


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_number(maxlen):
    symbols = '+' + string.digits + '-' * 2 + " " * 5
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_email(service, posfix, maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen))) + "@" + service + posfix


def random_month():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', '-']
    return random.choice(months)


def random_day():
    days = ['-'] + [str(i) for i in range(1, 32)]
    return random.choice(days)


#  чтение опций командной строки (из оф страницы)
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"


#  цикл для чтения опций (название опции, значение опции; хранятся в виде кортежей)
for o, a in opts:
    if o == "-n":  # опция == кол-ву контактов
        n = int(a)
    elif o == "-f":  # опция == названию файла
        f = a


test_data = [Contact(firstname='', middlename='', lastname='', nickname='', photo='', title='',
                     company='', address='', home_number='', mobile_number='', work_number='',
                     fax='', email='', email2='', email3='', homepage='', bday='', bmonth='-',
                     byear='', aday='', amonth='-', ayear='', address2='', phone2='', notes='')] + \
            [
                Contact(firstname=random_string('f', 5), middlename=random_string('m', 5), lastname=random_string('l', 5),
                        nickname=random_string('n', 5), photo='', title=random_string('title', 10), company=random_string('comp', 5),
                        address=random_string('address', 25), home_number=random_number(10), mobile_number=random_number(10), work_number=random_number(10),
                        fax=random_number(10), email=random_email("gmail", ".com", 20), email2=random_email("mail", ".ru", 20), email3=random_email("gmail", ".com", 20),
                        homepage=random_string("homepage", 5), bday=random_day(), bmonth=random_month(),
                        byear=random.randint(1900, 2050), aday=random_day(), amonth=random_month(), ayear=random.randint(1900, 2050),
                        address2=random_string("address2", 50), phone2=random_number(10), notes=random_string("address2", 150))
                for i in range(n)
]


# сначала берем абсолютный путь от файла __file__
# далее берем название дииректории, в котором нах-ся файл
# к директории приклеиваем значение из ".." + f
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)  # чтобы данные в json-файлых были красивенькие
    out.write(jsonpickle.encode(test_data)) # ета штука нужна чтобы к сгенерированным данным еще и дописывать имя класса
