import random
from pytest_bdd import given, when, then  # пометки
from model.group import Group


# STEPS FOR ADD GROUP
# предусловие
@given('a group list')  # эти штуки представляют собой фикстуры, а их можно передавать в кач-ве параметра, что мы сделали в ф-ции verify_group_added
def group_list(db):
    return db.get_group_list()


# предусловие
@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(group_name=name, group_header=header, group_footer=footer)


# действие
@when('I add the group to the list')  # это тоже фикстура
def add_new_group(app, new_group):
    app.group.create(new_group)


# постусловие
@then('the new group list is equal to the old list with the added group')  # и это тоже фикстура
def verify_group_added(db, group_list, new_group):
    old_groups_list = group_list
    new_groups_list = db.get_group_list()
    old_groups_list += [new_group]
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


# STEPS FOR DELETE GROUP
@given('a random group from group list')
def random_group(group_list):
    return random.choice(group_list)


@when('I delete the group from the list')  # это тоже фикстура
def del_some_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old list without deleted group')  # и это тоже фикстура
def verify_group_added(db, group_list, random_group):
    old_groups_list = group_list
    new_groups_list = db.get_group_list()
    old_groups_list.remove(random_group)
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


@given('a new group with <new_name>, <new_header> and <new_footer>')
def new_group_for_modify(new_name, new_header, new_footer):
    return Group(group_name=new_name, group_header=new_header, group_footer=new_footer)


@when('I modify the group from the list')  # это тоже фикстура
def modify_some_group(app, random_group, new_group_for_modify):
    app.group.modify_group_by_id(random_group.id, new_group_for_modify)


@then('the new group list is equal to the old list with modify group')  # и это тоже фикстура
def verify_group_added(db, group_list, random_group, new_group_for_modify):
    old_groups_list = group_list
    new_groups_list = db.get_group_list()
    old_groups_list.remove(random_group)
    old_groups_list += [new_group_for_modify]
    # res_old_groups = []
    # for i in range(len(old_groups_list)):
    #     if str(old_groups_list[i].id) != str(random_group.id):
    #         res_old_groups += [old_groups_list[i]]
    #     if str(old_groups_list[i].id) == str(random_group.id):
    #         res_old_groups += [new_group_for_modify]
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)
