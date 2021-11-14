class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
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
        self.app.return_to_home_page()

    def delete_first_group(self):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.app.return_to_home_page()

    def modify_first_group_name(self, new_name):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(new_name)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.app.return_to_home_page()

    def modify_first_group_header(self, new_header):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(new_header)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.app.return_to_home_page()

    def modify_first_group_footer(self, new_footer):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(new_footer)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.app.return_to_home_page()