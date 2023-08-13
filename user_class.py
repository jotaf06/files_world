class User():

    def __init__(self, login, nickname, password):
        self.online = 0
        self.login = login
        self.nickname = nickname
        self.password = password
        self.privacity = 0
        self.files = {}
        self.friends = []
        self.groups = []

    def change_nickname(self):
        pass

    def change_password(self):
        pass

    def adicionar_arquivos(self):
        pass

    def adicionar_amigos(self):
        pass

    def entrar_grupo(self):
        pass
