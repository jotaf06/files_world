from find_user_bynick_class import FindUser

class UserInfoGenerator():
    def __init__(self, users):
        self.users = users

    def find(self, nickname):
        FindUser(self.users, nickname).find()
    
    def new_nickname(self):
        """Determina um novo nickname válido"""
        nickname = input('\nDigite seu novo nickname: ')
        while True:
            if self.find(nickname) == None:
                print('\nnickname válido!!')
                return nickname
            else:
                print('\nEsse nickname ja existe')
                nickname = input('\nDigite um outro nickname: ')

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

    def new_password(self):
        return input('\nDigite sua senha: ')

    def generate_info(self):
        """Cria um novo usuário"""
        return self.new_login(), self.new_nickname(), self.new_password
        