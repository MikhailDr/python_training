# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(Contact(firstname="Wil", lastname="Wheaton"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
