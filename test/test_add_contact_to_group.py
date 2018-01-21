# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random



def test_modify_contact_name(app, dbORM):
    if len(dbORM.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Lili", lastname="Avarage"))
    if  len(dbORM.get_group_list()) == 0:
        app.group.create(Group(name="Women"))
    old_contact = dbORM.get_contact_list()
    old_group = dbORM.get_group_list()
    contact = random.choice(old_contact)
    group = random.choice(old_group)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_contact = dbORM.get_contacts_in_group(group)
    old_contact.remove(contact)
    assert sorted(new_contact, key=Contact.id_or_max) == sorted(dbORM.get_contacts_in_group(group), key=Contact.id_or_max)