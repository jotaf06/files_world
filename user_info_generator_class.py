from find_user_bynick_class import FindUser

class UserInfoGenerator():
    def __init__(self, users):
        self.users = users

    def new_login(self):
        """Determina um novo login válido"""
        login = input('\nDigite seu novo login: ')
        while True:
            if login not in self.users:
                print('Login válido!!')
                return login
            else:
                print('Esse login ja existe')
                login = input('\nDigite um outro login: ')

    def new_nickname(self):
        """Determina um novo nickname válido"""
        nickname = input('\nDigite seu novo nickname: ')
        while True:
            if FindUser().find(self.users, nickname) == None:
                print('\nnickname válido!!')
                return nickname
            else:
                print('\nEsse nickname ja existe')
                nickname = input('\nDigite um outro nickname: ')

    def new_password(self):
        return input('\nDigite sua senha: ')

    def create_user(self):
        """Cria um novo usuário"""
        user_login = self.new_login()
        user_nickname = self.new_nickname()
        user_password = self.new_password()
        return user_login, user_nickname, user_password
        