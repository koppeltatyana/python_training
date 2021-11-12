# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self): # функция инициализации
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="asd", header="asd", footer="asd")) # вместо передачи параметров передаем объект класса Group
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()

    def logout(self):
        wd = self.wd # получаем ссылку на драйвер из текущего объекта
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd # получаем ссылку на драйвер из текущего объекта
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill groups form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_id("content").click()
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()


    def open_groups_page(self):
        wd = self.wd # получаем ссылку на драйвер из текущего объекта
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd # получаем ссылку на драйвер из текущего объекта
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        wd = self.wd # получаем ссылку на драйвер из текущего объекта
        wd.get("http://localhost/addressbook/")

    def tearDown(self): # функция очистки после прохождения теста
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()