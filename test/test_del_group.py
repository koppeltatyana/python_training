import allure
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    # добавление проверки: если ни одной группы не существует, то перед удалением создаем таковую
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="Name", group_header="Header", group_footer="Footer"))
    with allure.step("Given non empty group list"):
        old_groups = db.get_group_list()
    with allure.step("Given a random group from non empty group list"):
        group = random.choice(old_groups)  # выбираем группу не по индексу, а из перечня доступных
    with allure.step("When I delete a group '{}' from the list".format(group)):
        app.group.delete_group_by_id(group.id)  # удаляем группу по id группы, так как сортировки списков групп в БД и ui разные
    with allure.step("Then the new group list is equal to the old list without deleted group"):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
