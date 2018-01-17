from model.contact import Contact
import random

def test_modify_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Lili", lastname="Avarage"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.modify_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact.remove(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
#