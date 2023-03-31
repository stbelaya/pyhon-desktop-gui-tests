class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        group_list = []
        self.open_group_editor()
        tree = self.select_group_tree()
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def select_group_tree(self):
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        return tree

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def del_some_group_by_name(self, group_name):
        self.open_group_editor()
        self.select_some_group_by_name(group_name)
        # press Delete button
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        # new window dialog "Delete group"
        self.delete_group_dialog = self.app.application.window(title="Delete group")
        # deletion option by default - Move contacts before group and subgroups deleting (to the top group)
        # press OK button
        self.delete_group_dialog.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def select_some_group_by_name(self, group_name):
        tree = self.select_group_tree()
        tree.get_item(f'\\Contact groups\\{group_name}').click()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def prepare_groups_preconditions(self):
        group_list = self.app.groups.get_group_list()
        if not group_list:
            self.app.groups.add_new_group("Group 1")
            self.app.groups.add_new_group("Group 2")
            group_list = self.app.groups.get_group_list()
        elif len(group_list) == 1:
            self.app.groups.add_new_group("Group 1")
            group_list = self.app.groups.get_group_list()
        return group_list
