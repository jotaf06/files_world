class FindUser():
    def find(self, users, nickname):
        """Procura o usuário que possui tal nickname"""
        for user in users.values():
            if user.nickname == nickname:
                return user
        return None