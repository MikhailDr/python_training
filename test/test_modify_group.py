from model.group import Group
import random

def test_modify__group_name(app, db, check_ui):
        if  len(db.get_group_list()) == 0:
            app.group.create(Group(name="Women"))
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        app.group.modify_group_by_id(group.id)
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups.remove(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                         key=Group.id_or_max)



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
