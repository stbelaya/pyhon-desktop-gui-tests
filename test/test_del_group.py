import random


def test_del_group_move_contacts(app):
    old_list = app.groups.prepare_groups_preconditions()
    group_name = random.choice(old_list)
    app.groups.del_some_group_by_name(group_name)
    new_list = app.groups.get_group_list()
    old_list.remove(group_name)
    assert sorted(old_list) == sorted(new_list)


# def test_del_group_del_contacts(app):
#     old_list = app.groups.get_group_list()
#     # we need 1 group to be deleted and 1 to stay
#     if not old_list:
#         app.groups.add_new_group("Group 1")
#         app.groups.add_new_group("Group 2")
#         old_list = app.groups.get_group_list()
#     elif len(old_list) == 1:
#         app.groups.add_new_group("Group 1")
#         old_list = app.groups.get_group_list()
#     group_name = random.choice(old_list)
#     app.groups.del_some_group_by_name(group_name)
#     new_list = app.groups.get_group_list()
#     old_list.remove(group_name)
#     assert sorted(old_list) == sorted(new_list)