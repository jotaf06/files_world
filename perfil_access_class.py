from find_user_bynick_class import FindUser

class PerfilAccess():
    def access(self, users, user):
        nickname = input("\nForneça o nickname do perfil: ")
        a_user = FindUser().find(users, nickname)

        if a_user == None:
            print("\nNão há usuário com esse perfil.")
        
        elif a_user.privacity == 1:
            print("\nEsse perfil é privado.")
            if user in a_user.friends:
                return a_user
            else:
                print("Você não tem acesso a esse perfil.")
                return None
    
        elif a_user.privacity == 0:
            print("\nEsse perfil é aberto.")
            return a_user


            
