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
    # загружаем списки контактов и групп, чтобы из них выбирать рандомную группу и контакт
    contacts_list = orm.get_contact_list()
    groups_list = orm.get_group_list()
    random_group = random.choice(groups_list)
    random_contact = random.choice(contacts_list)
    # старый список контактов, которые содержаться в группе random_group перед добавлением контакта в группу
    old_contacts_in_random_group_list = orm.get_contact_in_group(random_group)
    # меняем рандомную группу до тех пор, пока не найдем группу, в которой есть не все котакты
    while len(old_contacts_in_random_group_list) == len(contacts_list):
        groups_list.remove(random_group)
        random_group = random.choice(groups_list)
        old_contacts_in_random_group_list = orm.get_contact_in_group(random_group)

    # выбираем контакт до тех пор, пока не найдем контакт, который не состоит в random_group
    while random_contact in old_contacts_in_random_group_list:
        contacts_list.remove(random_contact)
        random_contact = random.choice(contacts_list)

    # добавляем random_contact в random_group
    app.contact.add_some_contact_to_some_group(random_contact, random_group)
    # новый список контактов, которые содержаться в группе random_group после добавления контакта в группу
    new_contacts_in_random_group_list = orm.get_contact_in_group(random_group)
    if random_contact not in old_contacts_in_random_group_list:
        old_contacts_in_random_group_list += [random_contact]
    assert sorted(old_contacts_in_random_group_list, key=Contact.id_or_max) == sorted(new_contacts_in_random_group_list, key=Contact.id_or_max)
