class UserInfoGenerator():
    def __init__(self, users):
        self.users = users

    def new_login_user(self):
        """Determina um novo login válido"""
        new_login = input('\nDigite seu novo login: ')
        while True:
            if new_login not in self.users:
                print('Login válido!!')
                return new_login
            else:
                print('Esse login ja existe')
                new_login = input('\nDigite um outro login: ')

    def find_user(self, new_nickname):
        """Procura o usuário que possui tal nickname"""
        for ouser in self.users.values():
            if ouser.nickname == new_nickname:
                return True
        return False

    def new_nickname_user(self):
        """Determina um novo nickname válido"""
        new_nickname = input('\nDigite seu novo nickname: ')
        while True:
            if self.find_user(new_nickname) == False:
                print('\nnickname válido!!')
                return new_nickname
            else:
                print('\nEsse nickname ja existe')
                new_nickname = input('\nDigite um outro nickname: ')

    def generate_info(self):
        """Cria um novo usuário"""
        user_login = self.new_login_user()
        user_nickname = self.new_nickname_user()
        user_password = input('\nDigite sua senha: ')
        return user_login, user_nickname, user_password
        