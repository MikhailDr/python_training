
from model.group import Group

def test_modification__group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification(Group (name="Women", header="Pink", footer="Nothing"))
    app.session.logout()