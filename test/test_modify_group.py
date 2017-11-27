
from model.group import Group

def test_modify__group_name(app):
    if not app.group.modify_first_group(Group(name="Women")):
        app.group.modify_first_group(Group(name="Women"))


def test_modify__group_header(app):
    if not app.group.modify_first_group(Group(header="Pink")):
        app.group.modify_first_group(Group(header="Pink"))


def test_modify__group_footer(app):
    if not app.group.modify_first_group(Group(footer="Nothing")):
        app.group.modify_first_group(Group(footer="Nothing"))
