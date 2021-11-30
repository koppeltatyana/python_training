from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # entering contact's form
        self.enter_values(contact)
        # click to the button "Enter"
        wd.find_element_by_xpath("//input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        # selecting first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # click to the button "Delete"
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accepting with alert on the window
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact):
        wd = self.app.wd
        self.app.return_to_home_page()
        # init contact editing
        self.select_contact_by_index_for_edit(index)
        self.enter_values(new_contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index_for_edit(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("tr > td:nth-child(8)")[index].click()

    #  функция заполнения полей
    def enter_values(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        # entering numbers
        self.change_field_value("home", contact.home_number)
        self.change_field_value("mobile", contact.mobile_number)
        self.change_field_value("work", contact.work_number)
        self.change_field_value("fax", contact.fax)
        # entering emails and homepage
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # entering data fields
        self.change_data_field_value("bday", contact.bday)
        self.change_data_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_data_field_value("aday", contact.aday)
        self.change_data_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        # entering secondary block
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_data_field_value(self, field_name, new_value):
        wd = self.app.wd
        # если пришло значение != значению по умолчанию, то меняем значение на новое
        if new_value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(new_value)

    def change_field_value(self, field_name, new_value):
        wd = self.app.wd
        # если пришло значение != значению по умолчанию, то меняем значение на новое
        if new_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(new_value)

    def count_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                contact_lastname = element.find_element_by_css_selector("tr > td:nth-child(2)").text
                contact_firstname = element.find_element_by_css_selector("tr > td:nth-child(3)").text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache += [Contact(contact_id=contact_id, lastname=contact_lastname, firstname=contact_firstname)]
        return list(self.contact_cache)  # возвращаем копию этого списка в случае поломки данных
