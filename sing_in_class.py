class SingIn():

    def __init__(self, users):
        self.users = users

    def non_existing_user(self):
        print("Usuário inexistente. Esse login não está cadastrado na rede.")
        print("Abordando operação sing_in...\n")
        return None
    
    def password_verification(self, ouser, password):
        """verifica se a senha passada da acesso ao usuário"""
        if ouser.password != password:
            print("Senha inválida!!!\n")
            return None
        else:            
            print("sing_in realizado com sucesso!\n")
            return ouser

    def signing_in(self):
        login = input("login: ")
        password = input("senha: ")

        if login not in self.users:
            self.non_existing_user()
        else:
            self.password_verification(self.users[login], password)
            
                