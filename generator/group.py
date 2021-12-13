import getopt  # чтение опций командной строки
import sys  # для получения опций командной строки
import random
import string
from model.group import Group
import os.path
import json


#  чтение опций командной строки (из оф страницы)
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/groups.json"

#  цикл для чтения опций (название опции, значение опции; хранятся в виде кортежей)
for o, a in opts:
    if o == "-n":  # опция == '-n' - кол-во групп
        n = int(a)
    elif o == "-f":  # опция == '-f' - файл, куда нужно писать данные
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


test_data = [Group(group_name="", group_header="", group_footer="")] + [
        Group(group_name=random_string('name', 5), group_header=random_string('header', 10), group_footer=random_string('footer', 20))
        for i in range(n)
    ]


# сначала берем абсолютный путь от файла __file__
# далее берем название дииректории, в котором нах-ся файл
# к директории приклеиваем значение из ".." + f
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    #  json.dumps превращает некоторый тип данных в строку
    #  __dict__ делает из json'а словарь (нужно, так как пакет json не знает как преобразовать объект типа Group в json)
    #  поэтому нужно указать функцию default
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))  # indent = 2 для красивого json'a
