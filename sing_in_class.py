class SingIn():

    def __init__(self, users):
        self.users = users

    def signing_in(self):
        login = input("login: ")
        password = input("senha: ")

        if login not in self.users:
            print("Usuário inexistente. Esse login não está cadastrado na rede.")
            print("Abordando operação sing_in...\n")
        else:
            ouser = self.users[login]
            if ouser.password != password:
                print("Senha inválida!!!\n")
            else:            
                print("sing_in realizado com sucesso!\n")
                ouser.online = 1
                