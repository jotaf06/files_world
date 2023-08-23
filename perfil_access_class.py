from find_user_bynick_class import FindUser

class PerfilAccess():
    def access(self, users, user):
        try:
            nickname = input("\nForneça o nickname do perfil: ")
            a_user = FindUser().find(users, nickname)

            if a_user == None:
                raise Exception("Não há usuário com esse perfil.")
            
            elif a_user.privacity == 1:
                print("Esse perfil é privado.")
                if user in a_user.friends:
                    return a_user
                else:
                    raise Exception("Você não tem acesso a esse perfil.")
        
            elif a_user.privacity == 0:
                print("\nEsse perfil é aberto.")
                return a_user
                
        except Exception as erro:
            print("Ocorreu um erro na operação de acesso: ", erro)

