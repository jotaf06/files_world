class User():
    def __init__(self, login, nickname, password):
        self.login = login
        self.nickname = nickname
        self.password = password
        self.privacity = 0
        self.friends = []
        self.groups = []

    def __str__(self):
        return f"***Debug***\n    login: {self.login}\n   nickname: {self.nickname}\n    password: {self.password}\n      privacity: {self.privacity}\n    friends: {self.friends}\n    groups: {self.groups}"
        
