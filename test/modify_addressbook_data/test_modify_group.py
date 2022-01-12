import allure
from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    # добавление проверки: если ни одной группы не существует, то перед удалением создаем таковую
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    with allure.step("Given non empty group list"):
        old_groups = db.get_group_list()
    with allure.step("Given a random group from non empty group list"):
        random_group = random.choice(old_groups)  # случайным образом выбираем группe для модификации
    with allure.step("Given a new group"):
        new_group = Group(group_name="New Name", group_header="New Header", group_footer="New Footer")
    with allure.step("When I modify a group {0} from the list with new data from group {1}".format(random_group, new_group)):
        app.group.modify_group_by_id(random_group.id, new_group)
    with allure.step("Then the new group list is equal to the old list with modify group"):
        old_groups[old_groups.index(random_group)] = new_group
        new_groups = db.get_group_list()
        assert old_groups == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
