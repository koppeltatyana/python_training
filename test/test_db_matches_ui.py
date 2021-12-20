from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):  # убираем наши лишние пробелы (только в нашем тесте)
        return Group(group_id=group.id, group_name=group.group_name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()

    def clean(contact):  # убираем наши лишние пробелы (только в нашем тесте)
        return Contact(contact_id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = list(map(clean, db.get_contact_list()))
    #  print(ui_list, db_list, sep="\n")
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
