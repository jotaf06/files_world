class GroupFinder():
    def find(self, groups, name):
        for group_name in groups:
            if name == group_name:
                return groups[group_name]
        return None