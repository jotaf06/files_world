class Finder():
    def __init__(self, users, groups):
        self.users = users
        self.groups = groups

    def find_member(self):
        pass

    def find_user(self, nickname):
        """Procura o usuário que possui tal nickname"""
        for user in self.users.values():
            if user.nickname == nickname:
                return user
        return None
    
    def find_group(self, name):
        """Procura um grupo pelo nome"""
        for group_name in self.groups:
            if name == group_name:
                return self.groups[group_name]
        return None