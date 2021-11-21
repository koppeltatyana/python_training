class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.group_header)
        self.change_field_value("group_footer", group.group_footer)

    def change_field_value(self, field_name, new_value):
        wd = self.app.wd
        # если новое значение параметра != значению по умолчанию, то записываем новое значение
        if new_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(new_value)

    def count_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
