import json
import os.path
from model.group import Group
from fixture.application import Application
from fixture.db import DbFixture


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="mozilla"):
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

    def create_group(self, name, header, footer):
        self.fixture.group.create(Group(group_name=name, group_header=header, group_footer=footer))
