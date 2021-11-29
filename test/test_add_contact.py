# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='Томас', middlename='Джеффри', lastname='Хэнкс',
                      nickname='Том', photo='', title='Номер Томми',
                      company='Голливуд', address='Лос-Анжелес',
                      home_number='111222333', mobile_number='+1465789159',
                      work_number='789456123', fax='546546546', email='thomas.hanks@gmail.com',
                      email2='tommi.king@gmail.com', email3='tfhanks@yahoo.com',
                      homepage='https://en.wikipedia.org/wiki/Tom_Hanks',
                      bday='10', bmonth='October', byear='1965',
                      aday='10', amonth='October', ayear='2025',
                      address2='Пляжная ул.', phone2='789456123', notes='Qweashgdfaghcxhgzctafsd')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts += [contact]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='', middlename='', lastname='', nickname='', photo='', title='',
                      company='', address='', home_number='', mobile_number='', work_number='',
                      fax='', email='', email2='', email3='', homepage='', bday='', bmonth='-',
                      byear='', aday='', amonth='-', ayear='', address2='', phone2='', notes='')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts += [contact]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
