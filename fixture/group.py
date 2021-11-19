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

        # entering group's form
        self.enter_group_values(group)

        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, new_group):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        # entering group's form with new data
        self.enter_group_values(new_group)
        # submit group updating
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def enter_group_values(self, group):
        wd = self.app.wd
        # если новое значение параметра != значению по умолчанию, то записываем новое значение
        if group.group_name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.group_name)

        if group.group_header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.group_header)

        if group.group_footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.group_footer)
