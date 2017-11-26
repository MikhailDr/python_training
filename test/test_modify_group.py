
from model.group import Group

def test_modify__group_name(app):
    app.group.modify_first_group(Group(name="Women"))


def test_modify__group_header(app):
    app.group.modify_first_group(Group(header="Pink"))


def test_modify__group_footer(app):
    app.group.modify_first_group(Group(footer="Nothing"))
