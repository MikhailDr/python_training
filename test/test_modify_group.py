
from model.group import Group

def test_modify__group_name(app):
        if app.group.count() == 0:
            app.group.create(Group(name="Women"))
        old_groups = app.group.get_group_list()
        group = Group(name="Women")
        group.id = old_groups[0].id
        app.group.modify_first_group(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify__group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="Pink"))
#       old_groups = app.group.get_group_list()
#       new_groups = app.group.get_group_list()
#        assert len(old_groups) == len(new_groups)


#def test_modify__group_footer(app):
#   if app.group.count() == 0:
#        app.group.create(Group(footer="Nothing"))
#       old_groups = app.group.get_group_list()
#        new_groups = app.group.get_group_list()
 #       assert len(old_groups) == len(new_groups)
