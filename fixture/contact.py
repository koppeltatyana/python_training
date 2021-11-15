from selenium.webdriver.support.select import Select
from model.contact import Contact
import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contacts form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_number)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_number)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # entering bday from picklist
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # entering anniversary day from picklist
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # entering secondary block
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//input[21]").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.return_to_home_page()

    def modify_first_contact(self, new_firstname='', new_middlename='', new_lastname='', new_nickname='', new_photo='', new_title='',
                             new_company='', new_address='', new_home_number='', new_mobile_number='',
                             new_work_number='', new_fax='', new_email='', new_email2='', new_email3='',
                             new_homepage='', new_bday='-', new_bmonth='-', new_byear='', new_aday='-', new_amonth='-',
                             new_ayear='', new_address2='', new_phone2='', new_notes=''):
        wd = self.app.wd

        # values_dictionary = {}

        self.app.return_to_home_page()
        # init contact creation
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        old_contact = Contact(firstname=wd.find_element_by_name("firstname").text, middlename=wd.find_element_by_name("middlename").text, lastname=wd.find_element_by_name("lastname").text,
                              nickname=wd.find_element_by_name("nickname").text, photo='', title=wd.find_element_by_name("title").text, company=wd.find_element_by_name("company").text,
                              address=wd.find_element_by_name("address").text, home_number=wd.find_element_by_name("home").text, mobile_number=wd.find_element_by_name("mobile").text,
                              work_number=wd.find_element_by_name("work").text, fax=wd.find_element_by_name("fax").text, email=wd.find_element_by_name("email").text,
                              email2=wd.find_element_by_name("email2").text, email3=wd.find_element_by_name("email3").text, homepage=wd.find_element_by_name("homepage").text,
                              bday=wd.find_element_by_name("bday").text, bmonth=wd.find_element_by_name("bmonth").text, byear=wd.find_element_by_name("byear").text,
                              aday=wd.find_element_by_name("aday").text, amonth=wd.find_element_by_name("amonth").text, ayear=wd.find_element_by_name("ayear").text,
                              address2=wd.find_element_by_name("address2").text, phone2=wd.find_element_by_name("phone2").text, notes=wd.find_element_by_name("notes").text)
        time.sleep(2)
        #  fill contacts form
        # enter the new firstname's information
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        if new_firstname == '':
            wd.find_element_by_name("firstname").send_keys(old_contact.firstname)
        else:
            wd.find_element_by_name("firstname").send_keys(new_firstname)

        # enter the new middlename's information
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        if new_middlename == '':
            wd.find_element_by_name("middlename").send_keys(old_contact.middlename)
        else:
            wd.find_element_by_name("middlename").send_keys(new_middlename)

        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        if new_lastname == '':
            wd.find_element_by_name("lastname").send_keys(old_contact.lastname)
        else:
            wd.find_element_by_name("lastname").send_keys(new_lastname)

        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        if new_nickname == '':
            wd.find_element_by_name("nickname").send_keys(old_contact.nickname)
        else:
            wd.find_element_by_name("nickname").send_keys(new_nickname)

        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        if new_title == '':
            wd.find_element_by_name("title").send_keys(old_contact.title)
        else:
            wd.find_element_by_name("title").send_keys(new_title)

        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        if new_company == '':
            wd.find_element_by_name("company").send_keys(old_contact.company)
        else:
            wd.find_element_by_name("company").send_keys(new_company)

        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        if new_address == '':
            wd.find_element_by_name("address").send_keys(old_contact.address)
        else:
            wd.find_element_by_name("address").send_keys(new_address)

        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        if new_home_number == '':
            wd.find_element_by_name("home").send_keys(old_contact.home_number)
        else:
            wd.find_element_by_name("home").send_keys(new_home_number)

        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        if new_mobile_number == '':
            wd.find_element_by_name("mobile").send_keys(old_contact.mobile_number)
        else:
            wd.find_element_by_name("mobile").send_keys(new_mobile_number)

        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        if new_work_number == '':
            wd.find_element_by_name("work").send_keys(old_contact.work_number)
        else:
            wd.find_element_by_name("work").send_keys(new_work_number)

        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        if new_fax == '':
            wd.find_element_by_name("fax").send_keys(old_contact.fax)
        else:
            wd.find_element_by_name("fax").send_keys(new_fax)

        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        if new_email == '':
            wd.find_element_by_name("email").send_keys(old_contact.email)
        else:
            wd.find_element_by_name("email").send_keys(new_email)

        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        if new_email2 == '':
            wd.find_element_by_name("email2").send_keys(old_contact.email2)
        else:
            wd.find_element_by_name("email2").send_keys(new_email2)

        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        if new_email3 == '':
            wd.find_element_by_name("email3").send_keys(old_contact.email3)
        else:
            wd.find_element_by_name("email3").send_keys(new_email3)

        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        if new_homepage == '':
            wd.find_element_by_name("homepage").send_keys(old_contact.homepage)
        else:
            wd.find_element_by_name("homepage").send_keys(new_homepage)

        # # entering bday from picklist
        wd.find_element_by_name("bday").click()
        if new_bday == '-':
            Select(wd.find_element_by_name("bday")).select_by_visible_text(old_contact.bday)
        else:
            Select(wd.find_element_by_name("bday")).select_by_visible_text(new_bday)

        wd.find_element_by_name("bmonth").click()
        if new_bmonth == '-':
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(old_contact.bmonth)
        else:
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(new_bmonth)

        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        if new_byear == '':
            wd.find_element_by_name("byear").send_keys(old_contact.byear)
        else:
            wd.find_element_by_name("byear").send_keys(new_byear)

        # entering anniversary day from picklist
        wd.find_element_by_name("aday").click()
        if new_aday == '-':
            Select(wd.find_element_by_name("aday")).select_by_visible_text(old_contact.aday)
        else:
            Select(wd.find_element_by_name("aday")).select_by_visible_text(new_aday)

        wd.find_element_by_name("amonth").click()
        if new_amonth == '-':
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(old_contact.amonth)
        else:
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(new_amonth)

        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        if new_ayear == '':
            wd.find_element_by_name("ayear").send_keys(old_contact.ayear)
        else:
            wd.find_element_by_name("ayear").send_keys(new_ayear)

        # entering secondary block
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        if new_address2 == '':
            wd.find_element_by_name("address2").send_keys(old_contact.address2)
        else:
            wd.find_element_by_name("address2").send_keys(new_address2)

        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        if new_phone2 == '':
            wd.find_element_by_name("phone2").send_keys(old_contact.phone2)
        else:
            wd.find_element_by_name("phone2").send_keys(new_phone2)

        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        if new_notes == '':
            wd.find_element_by_name("notes").send_keys(old_contact.notes)
        else:
            wd.find_element_by_name("notes").send_keys(new_notes)
        wd.find_element_by_xpath("//input[21]").click()
        self.app.return_to_home_page()
