import allure
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm):

    if len(orm.get_group_list()) == 0:  # проверка наличия групп
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    if len(orm.get_contact_list()) == 0:  # проверка наличия контактов
        app.contact.create(Contact(firstname="firstname", lastname="lastname", title="title"))
    with allure.step("Given a random group from non empty group list"):
        random_group = random.choice(orm.get_group_list())
    with allure.step("Given contacts which are not in random group"):
        contacts_not_in_group_list = orm.get_contacts_not_in_group(random_group)  # загружаем список к-ов, в группе не состоящих
    if len(contacts_not_in_group_list) == 0:
        with allure.step("If group has all existed contacts, I'll add a new contact"):
            new_contact = Contact(firstname="New Firstname")
            app.contact.create(new_contact)
            contacts_not_in_group_list = orm.get_contacts_not_in_group(random_group)
    with allure.step("Given random contact from contacts which are not in this group"):
        random_contact = random.choice(contacts_not_in_group_list)
    with allure.step("Given old contacts list which random group has"):
        old_contacts_in_random_group_list = orm.get_contacts_in_group(random_group)
    with allure.step("I add contact '{0}' to group '{1}'".format(random_contact, random_group)):
        app.contact.add_some_contact_to_some_group(random_contact, random_group)  # добавляем random_contact в random_group
    with allure.step("Then the new contacts list of group is equal to the old contacts list of group with adding contact"):
        new_contacts_in_random_group_list = orm.get_contacts_in_group(random_group)  # новый список контактов, которые содержаться в группе random_group после добавления контакта в группу
        old_contacts_in_random_group_list += [random_contact]
        assert sorted(old_contacts_in_random_group_list, key=Contact.id_or_max) == sorted(new_contacts_in_random_group_list, key=Contact.id_or_max)
