import json
import os.path
from model.group import Group
from fixture.application import Application
from fixture.db import DbFixture
import random


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as file:
            self.target = json.load(file)

    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])  # создание фикстуры
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        db_config = self.target["db"]
        self.db_fixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                               password=db_config["password"])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.db_fixture.destroy()

    def get_group_list(self):
        return self.db_fixture.get_group_list()

    def new_group(self, name, header, footer):
        return Group(group_name=name, group_header=header, group_footer=footer)

    def create_group(self, group):
        self.fixture.group.create(group)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def give_random_group_from_list(self, groups_list):
        if len(self.db_fixture.get_group_list()) == 0:
            self.fixture.group.create(Group(group_name="NAME"))
            groups_list += [Group(group_name="NAME")]
        return random.choice(groups_list)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def modify_group(self, group_for_modify, new_group):
        self.fixture.group.modify_group_by_id(group_for_modify.id, new_group)

    def replace_old_group_to_new_group(self, groups_list, old_value, new_value):
        groups_list[groups_list.index(old_value)] = new_value

