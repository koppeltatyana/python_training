import datetime
from pony.orm import *
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()  # Объект, на основе которого будет строится привязка

    # привязка
    class ORMGroup(db.Entity):
        _table_ = 'group_list'  # указываем название таблицы
        id = PrimaryKey(int, column='group_id')  # column указывается, когда названия переменных не соответствует атрибутам в таблице
        group_name = Optional(str, column='group_name')
        group_header = Optional(str, column='group_header')
        group_footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()  # сопоставление классов с данными в таблицах
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(group_id=str(group.id), group_name=group.group_name, group_header=group.group_header, group_footer=group.group_footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(contact_id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact))  #  if c.deprecated is None

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if orm_group not in c.groups))
