# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new_contact(Contacts(firstname="Mike", middlename="Sedrick", lastname="Dashman", nickname="Miki", title="Finger", company="MIT", address="CA, Los Altos, 24", home="none",
                               mobile="1234567890", workphone="(213)1235467", fax="none", email="alo1@ya.com", email2="mk@mit.com", email3="none",
                               homepage="www.sedrick.com", birthday="//div[@id='content']/form/select[1]//option[20]",
                               birthmonth="//div[@id='content']/form/select[2]//option[6]", birthyear="1986",
                               anniday="//div[@id='content']/form/select[3]//option[20]",
                               annimonth="//div[@id='content']/form/select[4]//option[6]", anniyear="2026", address2="CA, Los Altos, Hrandi, 25",
                               homephone2="Campos", notes="none"))
    app.session.logout()
