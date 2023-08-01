import os
from singning_up_class import SingInUP

class PerfilAccess:
    def run(self, user_login, users, friendships):
        """Mostra as informações associadas a um perfil com base no nickname fornecido"""
        while True:
            perfil_nickname = input("\nForneça o nickname do perfil: ")
            sing_up = SingInUP()
            user_login_sought = sing_up.find_user(users, perfil_nickname)

            if user_login_sought is None:
                print("\nNão há usuário com esse perfil.")
            elif users[user_login_sought]['privacity'] == 1:
                print("\nEsse perfil é privado.")
                
                if users[user_login]['nickname'] in friendships[user_login_sought]:
                    perfil_dir = os.path.join('files_world', users[user_login_sought]['nickname'])
                    
                    if not os.path.exists(perfil_dir):
                        print("Não há arquivos no perfil.")
                    else:
                        files = os.listdir(perfil_dir)
                        if len(files) == 0:
                            print("Não há arquivos no perfil.")
                        else:
                            print("Arquivos no perfil:")
                            for file in files:
                                print(file)
                else:
                    print("Você não tem acesso a esse perfil.")

            elif users[user_login_sought]['privacity'] == 0:
                print("\nEsse perfil é aberto.")

                perfil_dir = os.path.join('files_world', users[user_login_sought]['nickname'])
                print(perfil_dir)
                if not os.path.exists(perfil_dir):
                    print("\nNão há arquivos no perfil.")

                else:
                    files = os.listdir(perfil_dir)
                    if len(files) == 0:
                        print("Não há arquivos no perfil.")
                    else:
                        print("Arquivos no perfil:")
                        for file in files:
                            print(file)
                    
            continuar = input("\nDigite 'True' para continuar ou 'False' para parar a operação: ")
            if continuar.lower() != 'true':
                break
