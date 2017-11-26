# -*- coding: utf-8 -*-
from model.group import Group

    
def test_add_group(app):
    app.group.create(Group (name="People", header="example1", footer="Hi all this book"))

def test_add_empty_group(app):
    app.group.create(Group (name="", header="", footer=""))
