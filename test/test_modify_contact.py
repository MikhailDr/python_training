from model.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count_contact() == 0:
        app.contact.modify_first_contact(
            Contact(firstname="Lili", lastname="Avarage"))
        old_contact = app.contact.get_contact_list()
        contact = Contact(firstname="Lili", lastname="Avarage")
        contact.id = old_contact[0].id
        app.contact.modify_first_contact(contact)
        new_contact = app.contact.get_contact_list()
        assert len(old_contact) == len(new_contact)
        old_contact[0] = contact
        assert sorted(old_contact, key=contact.id_or_max) == sorted(new_contact, key=contact.id_or_max)
