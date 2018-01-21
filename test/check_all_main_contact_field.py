import re
from model.contact import Contact
import random


def test_contact_on_home_page_with_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        contact_from_db = contacts_from_db[i]
        contact_from_home_page = contacts_from_home_page[i]
        assert clear(contact_from_home_page.firstname) == clear(contact_from_db.firstname)
        assert clear(contact_from_home_page.lastname) == clear(contact_from_db.lastname)
        assert clear(contact_from_home_page.address) == clear(contact_from_db.address)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_db)


#def test_contact_on_home_page(app):
#    contact_from_home_page = app.contact.get_contact_list()[0]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.address == contact_from_edit_page.address
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.home == contact_from_edit_page.home
#    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#    assert contact_from_view_page.homephone2 == contact_from_edit_page.homephone2

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.workphone, contact.homephone2]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))