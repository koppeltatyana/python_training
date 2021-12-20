from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group):
        wd = self.app.wd  # получаем ссылку на драйвер из текущего объекта
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # entering group's form with new data
        self.enter_group_values(new_group)
        # submit group updating
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='{0}']".format(id)).click()

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

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache += [Group(group_name=text, group_id=group_id)]
        return list(self.group_cache)  # возвращаем копию этого списка в случае поломки данных
