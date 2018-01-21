from fixture.orm import ORMfixture
from model.group import Group


db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="123456")

try:
    l = db.get_contacts_not_in_group(Group(id=45))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

#    db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="123456")
#
#    try:
#        l = db.get_contact_list()
#        for item in l:
#            print(item)
#        print(len(l))
#    finally:
#        pass




#    from fixture.db import DbFixture
#
#    db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="123456")
#
#    try:
#        contacts = db.get_contact_list()
#        for contact in contacts:
#            print(contact)
#        print(len(contacts))
#    finally:
#        db.destroy()


# import pymysql.cursors

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="123456")

#try:
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():
#        print(row)
#finally:
#    connection.close()