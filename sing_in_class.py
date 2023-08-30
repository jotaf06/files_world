class SingIn():
    def __init__(self, users):
        self.users = users

    def non_existing_user(self):
        print("Usuário inexistente. Esse login não está cadastrado na rede.")
        print("Abordando operação sing_in...\n")
        return None        

    def signing_in(self):
        login = input("login: ")
        password = input("senha: ")

        if login not in self.users:
            self.non_existing_user()
        else:
            ouser = self.users[login]
            if ouser.password != password:
                print("Senha inválida!!!\n")
                return None
            else:            
                print("sing_in realizado com sucesso!\n")
                return ouser
            
                