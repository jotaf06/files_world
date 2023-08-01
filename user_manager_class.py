from data_manager_class import DataManager
from edit_user_class import UserEdit

class UsersManager(DataManager):
    def __init__(self):
        super().__init__('users.json')

    def entrando_na_rede(self, user_login):
            """Aqui ocorre toda a interação do usuário com a rede""" 

            users = self.load_data()
            user = users[user_login]         
            print(f"Olá {user['nickname']} Você está conectado a rede.")
            
            sair_da_rede = False
            while sair_da_rede == False:
                print("\nDigite 'lista_de_comandos', para ver os comandos da rede.\n")
                command = input("comando : ")

                if command == "lista_de_comandos":
                    self.lista_de_comandos()
                    
                elif command == 'editar_usuario':
                    edit_user = UserEdit(users, user_login)
                    print(user_login)
                    edit_user.edit_user()
                    self.save_data(users)

                elif command == 'acessar_perfil':
                    self.show_perfil()

                elif command == 'add_amigo':
                    self.adiciona_amigo()

                elif command == 'subir_arquivo':
                    self.upload_arquivo()
                    
                elif command == 'criar_grupo':
                    self.criar_grupo()

                elif command == 'entrar_grupo':
                    self.entrar_grupo()

                elif command == 'sair':
                    sair_da_rede = True
                    print("Desconectando...\n")

    def lista_de_comandos(self):
        print("\n'editar_usuario' - edita as informações associadas a um usuário.")
        print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
        print("'add_amigo' - adiciona um amigo.")
        print("'subir_arquivo' - subir conteúdo no perfil.")
        print("'criar_grupo' - cria um grupo.")
        print("'entrar_grupo' - entrar em um grupo.")
        print("'sair' - para se desconectar.")
