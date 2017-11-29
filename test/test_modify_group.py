
from model.group import Group

def test_modify__group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Women"))


def test_modify__group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Pink"))


def test_modify__group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="Nothing"))
