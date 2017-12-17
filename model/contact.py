from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                            address=None, home=None, mobile=None, workphone=None, fax=None, email=None, email2=None,
                            email3=None, homepage=None, birthday=None, birthmonth=None, birthyear=None, anniday=None,
                          annimonth=None, anniyear=None, address2=None, homephone2=None, notes=None, id=None, all_phones_from_home_page=None, all_email_from_home_page=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear
        self.anniday = anniday
        self.annimonth = annimonth
        self.anniyear = anniyear
        self.address2 = address2
        self.homephone2 = homephone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize