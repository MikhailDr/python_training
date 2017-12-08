from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create_new_contact(self, Contact):
        wd = self.app.wd
        # add_new_member
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        # send_member_form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, Contact):
        wd = self.app.wd
        self.change_field_value("firstname", Contact.firstname)
        self.change_field_value("middlename", Contact.middlename)
        self.change_field_value("lastname", Contact.lastname)
        self.change_field_value("nickname", Contact.nickname)
        self.change_field_value("title", Contact.title)
        self.change_field_value("company", Contact.company)
        self.change_field_value("address", Contact.address)
        self.change_field_value("home", Contact.home)
        self.change_field_value("mobile", Contact.mobile)
        self.change_field_value("work", Contact.workphone)
        self.change_field_value("fax", Contact.fax)
        self.change_field_value("email", Contact.email)
        self.change_field_value("email2", Contact.email2)
        self.change_field_value("email3", Contact.email3)
        self.change_field_value("homepage", Contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[20]").is_selected():
            wd.find_element_by_xpath(Contact.birthday).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[6]").is_selected():
            wd.find_element_by_xpath(Contact.birthmonth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.birthyear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[20]").is_selected():
            wd.find_element_by_xpath(Contact.anniday).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").is_selected():
            wd.find_element_by_xpath(Contact.annimonth).click()
        self.change_field_value("ayear", Contact.anniyear)
        self.change_field_value("address2", Contact.anniyear)
        self.change_field_value("phone2", Contact.homephone2)
        self.change_field_value("notes", Contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # delete first contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        self.open_modification_form()
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def count_contact(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            firstname = element.text
            lastname = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts