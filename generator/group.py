import getopt
import random
import string
import sys
from model.group import Group
import os.path
import json


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


test_data = [Group(group_name="", group_header="", group_footer="")] + [
        Group(group_name=random_string('name', 5), group_header=random_string('header', 10), group_footer=random_string('footer', 20))
        for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
