import random
import string
from model.group import Group


constant = [
    Group(group_name="group_name1", group_header="group_header1", group_footer="group_footer1"),
    Group(group_name="group_name2", group_header="group_header2", group_footer="group_footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


test_data = [Group(group_name="", group_header="", group_footer="")] + [
        Group(group_name=random_string('name', 5), group_header=random_string('header', 10), group_footer=random_string('footer', 20))
        for i in range(8)
    ]
