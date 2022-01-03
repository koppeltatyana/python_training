from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm):
    # проверка наличия групп
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    # проверка наличия контактов
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname", title="title"))

    groups_list = orm.get_group_list()
    # рандомная группа для удаления контакта из этой группы
    random_group = random.choice(groups_list)
    # старый список контактов, которые содержаться в группе random_group перед добавлением контакта в группу
    old_contacts_in_random_group_list = orm.get_contacts_in_group(random_group)

    # проверка, что в группе есть контакты, если нет, то добавляем контакт в группу
    if len(old_contacts_in_random_group_list) == 0:
        contacts_list = orm.get_contact_list()
        # рандомный контакт для добавления этого контакта в случае, если в рандомной группе нет контактов
        random_contact_from_all_contacts = random.choice(contacts_list)

        app.contact.add_some_contact_to_some_group(random_contact_from_all_contacts, random_group)
        old_contacts_in_random_group_list = orm.get_contacts_in_group(random_group)
    # рандомный контакт из списка контактов рандомной группы
    random_contact = random.choice(old_contacts_in_random_group_list)
    # удаляем контакт из группы
    app.contact.delete_some_contact_from_some_group(random_contact, random_group)
    new_contacts_in_random_group_list = orm.get_contacts_in_group(random_group)
    # убираем контакт из старого списка контактов в группе для сравнения списков
    old_contacts_in_random_group_list.remove(random_contact)
    assert sorted(old_contacts_in_random_group_list, key=Contact.id_or_max) == sorted(new_contacts_in_random_group_list, key=Contact.id_or_max)
