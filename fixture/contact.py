import re

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
        self.open_contact_by_index_for_edit(index)
        self.enter_values(new_contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

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

    def open_contact_by_index_for_edit(self, index):
        wd = self.app.wd
        # в таблице на главной странице нажимаем на иконку карандаша в 8 столбце
        wd.find_elements_by_css_selector("tr > td:nth-child(8)")[index].click()

    def open_contact_by_index_for_view(self, index):
        wd = self.app.wd
        # в таблице на главной странице нажимаем на иконку человечка в 7 столбце
        wd.find_elements_by_css_selector("tr > td:nth-child(7)")[index].click()

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
                all_phones = element.find_element_by_css_selector("tr > td:nth-child(6)").text
                all_emails = element.find_element_by_css_selector("tr > td:nth-child(5)").text
                self.contact_cache += [Contact(contact_id=contact_id, lastname=contact_lastname,
                                               firstname=contact_firstname, all_phones_from_home_page=all_phones,
                                               all_emails_from_home_page=all_emails)]
        return list(self.contact_cache)  # возвращаем копию этого списка в случае поломки данных

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.open_contact_by_index_for_edit(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_number = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(contact_id=contact_id, firstname=firstname, middlename=middlename,
                       lastname=lastname, home_number=home_number, work_number=work_number,
                       mobile_number=mobile_number, phone2=secondary_number,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.open_contact_by_index_for_view(index)
        text = wd.find_element_by_id("content").text
        fullname = wd.find_element_by_xpath("//div[@id='content']/b").text
        home_number = self.contact_number_on_view_page('H', text)
        work_number = self.contact_number_on_view_page('W', text)
        mobile_number = self.contact_number_on_view_page('M', text)
        secondary_number = self.contact_number_on_view_page('P', text)
        full_emails = self.get_all_emails_on_view_page(text)
        # print(full_emails)
        return Contact(fullname=fullname, home_number=home_number, work_number=work_number,
                       mobile_number=mobile_number, phone2=secondary_number, all_emails_from_view_page=full_emails)

    def contact_number_on_view_page(self, number_template, text):
        wd = self.app.wd
        if re.search("{0}:(.*)".format(number_template), text) is not None:
            number_from_view_page = re.search("{0}: (.*)".format(number_template), text).group(1)
        else:
            number_from_view_page = None
        return number_from_view_page

    def get_all_emails_on_view_page(self, text):
        wd = self.app.wd
        if re.findall("(.*@.+.[ru,com])", text) is not None:
            emails_from_view_page = re.findall("(.+@.+.[ru,com])", text)  # .group(1)
        else:
            emails_from_view_page = None
        return emails_from_view_page
