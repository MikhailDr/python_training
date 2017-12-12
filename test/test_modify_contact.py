from model.contact import Contact
from random import randrange

def test_modify_contact_name(app):
    if app.contact.count_contact() == 0:
        app.contact.modify_first_contact(
            Contact(firstname="Lili", lastname="Avarage"))
        old_contact = app.contact.get_contact_list()
        index = randrange(len(old_contact))
        contact = Contact(firstname="Lili", lastname="Avarage")
        contact.id = old_contact[index].id
        app.contact.modify_contact_by_index(contact, index)
        new_contact = app.contact.get_contact_list()
        assert len(old_contact) == len(new_contact)
        old_contact[index] = contact
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
