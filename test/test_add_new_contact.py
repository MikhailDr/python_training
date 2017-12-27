# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_new_contact import testdata

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_add_new_contact(app):
#    old_contact = app.contact.get_contact_list()
#    contact = Contact(firstname="Wil", lastname="Wheaton")
#    app.contact.create_new_contact(contact)
#    new_contact = app.contact.get_contact_list()
#    assert len(old_contact) + 1 == len(new_contact)
#    old_contact.append(contact)
#    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

