class User():
    def __init__(self, login, nickname, password):
        self.login = login
        self.nickname = nickname
        self.password = password
        self.privacity = 0
        self.files = {}
        self.friends = []
        self.groups = []
