from data_manager_class import DataManager, FriendshipManager, GroupsManager
from edit_user_class import UserEditor
from perfil_access_class import PerfilAccess
from upload_class import UploadArch

class UsersManager(DataManager):
    def __init__(self):
        super().__init__('users.json')
        self.users = self.load_data()

        self.friendships_manager = FriendshipManager()
        self.friendships = self.friendships_manager.load_data()

        self.groups_manager = GroupsManager()
        self.groups = self.groups_manager.load_data()

    def entrando_na_rede(self, user_login):
            """Aqui ocorre toda a interação do usuário com a rede""" 
            user = self.users[user_login]         
            print(f"Olá {user['nickname']} Você está conectado a rede.")
            
            sair_da_rede = False
            while sair_da_rede == False:
                print("\nDigite 'lista_de_comandos', para ver os comandos da rede.\n")
                command = input("comando : ")

                if command == "lista_de_comandos":
                    self.lista_de_comandos()
                    
                elif command == 'editar_usuario':
                    self.edit_user(user_login)

                elif command == 'acessar_perfil':
                    self.perfil_access(user_login)

                elif command == 'add_amigo':
                    self.adiciona_amigo(user_login)

                elif command == 'subir_arquivo':
                    self.upload_arquivo(user_login)
                    
                elif command == 'criar_grupo':
                    self.criar_grupo(user_login)

                elif command == 'entrar_grupo':
                    self.entrar_grupo(user_login)

                elif command == 'sair':
                    sair_da_rede = True
                    print("Desconectando...\n")

    def edit_user(self, user_login):
        user_editor = UserEditor(user_login, self.users)
        user_editor.edit_user()
        self.save_data(self.users)

    def perfil_access(self, user_login):
        perfil_access = PerfilAccess()
        perfil_access.run(user_login, self.users, self.friendships)

    def adiciona_amigo(self, user_login):
        self.friendships_manager.adiciona_amigo(user_login, self.friendships)
        self.friendships_manager.save_data(self.friendships)

    def upload_arquivo(self, user_login):
        user_nickname = self.users[user_login]['nickname']
        upload_manager = UploadArch()
        upload_manager.upload_arquivo(user_nickname)

    def criar_grupo(self, user_login):
        self.groups_manager.criar_grupo(self.users[user_login]['nickname'])

    def entrar_grupo(self, user_login):
        self.groups_manager.entrar_grupo(self.users, user_login, self.groups)


    def lista_de_comandos(self):
        print("\n'editar_usuario' - edita as informações associadas a um usuário.")
        print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
        print("'add_amigo' - adiciona um amigo.")
        print("'subir_arquivo' - subir conteúdo no perfil.")
        print("'criar_grupo' - cria um grupo.")
        print("'entrar_grupo' - entrar em um grupo.")
        print("'sair' - para se desconectar.")
