class FindUser():
    def __init__(self, users, groups):
        self.users = users
        self.groups = groups
    
    def find_member(self, nickname):
        pass

    def find_user(self, nickname):
        """Procura o usuário que possui tal nickname"""
        for user in self.users.values():
            if user.nickname == nickname:
                return user
        return None