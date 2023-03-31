import random


def test_del_group(app):
    old_list = app.groups.prepare_groups_preconditions()
    group_name = random.choice([group for group in old_list if group != "Contact groups"])
    # option to move or delete contacts is set randomly
    app.groups.del_some_group_by_name(group_name, move_contacts=random.choice([True, False]))
    new_list = app.groups.get_group_list()
    old_list.remove(group_name)
    assert sorted(old_list) == sorted(new_list)
