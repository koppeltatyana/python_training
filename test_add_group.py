# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self): # функция инициализации
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/group.php")
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        # open group page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("asd")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("asd")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("asd")
        wd.find_element_by_id("content").click()
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        wd.find_element_by_link_text("group page").click()
        # logout
        wd.find_element_by_link_text("Logout").click()

    
    def tearDown(self): # функция очистки после прохождения теста
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()