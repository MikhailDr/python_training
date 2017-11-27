from model.contact import Contact

def test_modification_contact(app):
    if not app.contact.modification_contact(
        Contact(firstname="Lili", middlename="Sanders", lastname="", nickname="Mini", title="Apple",
                 company="Apple", address="CA, Los Altos, 142", home="none",
                 mobile="1234567890", workphone="(213)3123213", fax="none", email="mini@ya.com", email2="mini@apple.com",
                 email3="none",
                 homepage="www.mini.com", birthday="//div[@id='content']/form/select[1]//option[13]",
                 birthmonth="//div[@id='content']/form/select[2]//option[9]", birthyear="1999",
                 anniday="//div[@id='content']/form/select[3]//option[13]",
                 annimonth="//div[@id='content']/form/select[4]//option[9]", anniyear="2009",
                 address2="CA, Los Altos, Hrandi, 143-1",
                 homephone2="Lampos", notes="none")):
        app.contact.modification_contact(
        Contact(firstname="Lili", middlename="Sanders", lastname="", nickname="Mini", title="Apple",
                 company="Apple", address="CA, Los Altos, 142", home="none",
                 mobile="1234567890", workphone="(213)3123213", fax="none", email="mini@ya.com", email2="mini@apple.com",
                 email3="none",
                 homepage="www.mini.com", birthday="//div[@id='content']/form/select[1]//option[13]",
                 birthmonth="//div[@id='content']/form/select[2]//option[9]", birthyear="1999",
                 anniday="//div[@id='content']/form/select[3]//option[13]",
                 annimonth="//div[@id='content']/form/select[4]//option[9]", anniyear="2009",
                 address2="CA, Los Altos, Hrandi, 143-1",
                 homephone2="Lampos", notes="none"))
