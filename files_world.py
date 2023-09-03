from user_class import User
from group_class import Group
from perfil_files_manager_class import PerfilFilesManager

ouser1 = User("vini1", "king1", "123")
ouser2 = User("vini2", "king2", "123")
ouser3 = User("vini3", "king3", "123")

group1 = Group(ouser1, "king_group1")
ouser1.groups = group1

users = [ouser1, ouser2, ouser3]
groups = [group1]

class FilesWorld():
    def __init__(self):
        self.manager = PerfilFilesManager()

    def edition_commands(self):
        print("'editar_usuario' - edita as informações associadas a um usuário.")
        print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
        print("'add_amigo' - adiciona um amigo.")
        print("'subir_arquivo' - subir conteúdo no perfil.")
        print("'criar_grupo' - cria um grupo.")
        print("'entrar_grupo' - entrar em um grupo.")
        print("'sair' - para se desconectar.\n")

    def user_edition(self, user):
        print("Você está na área de edição das informações de seu usuário\n")
        print("Digite 'comandos' para ver os comandos de edição")

        while True:
            command = input("comando: ")
            if command == 'comandos':
                self.edition_commands()
            elif command == 'login':
                user.edit_login(users)
            elif command == 'nickname':
                user.edit_nickname(users)
            elif command == 'senha':
                user.edit_password()
            elif command == 'editar_privacidade':
                user.edit_privacity()
            elif command == 'delecao_de_conta':
                user.del_user(users)
            elif command == 'sair':
                print(user)
                break

    def session_commands(self):
        print("'editar_usuario' - edita as informações associadas a um usuário.")
        print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
        print("'add_amigo' - adiciona um amigo.")
        print("'subir_arquivo' - subir conteúdo no perfil.")
        print("'criar_grupo' - cria um grupo.")
        print("'entrar_grupo' - entrar em um grupo.")
        print("'sair' - para se desconectar.\n")

    def session_init(self, user):

        print(f"Olá {user.nickname} Você está conectado a rede.")
        print("Digite 'lista_de_comandos' para ver os comandos da rede\n")
        
        while True:    
            command = input("comando : ")
            if command == 'lista_de_comandos':
                self.session_commands()
            elif command == 'editar_usuario':
                self.user_edition(user)
            elif command == 'acessar_perfil':
                nickname = input("Forneça o nickname do perfil que você deseja acessar: ")
                for a_user in users:
                    if a_user.nickname == nickname:
                        self.manager.acessing(a_user) 
            elif command == 'add_amigo':
                nickname = input("Forneça o nickname do seu novo amigo: ")
                for a_user in users:
                    if a_user.nickname == nickname:
                        user.add_amigo(a_user)
            elif command == 'subir_arquivo':
                self.manager.uploading(user)
            elif command == 'criar_grupo':
                self.group_creation(user)
            elif command == 'entrar_grupo':
                self.entrar_grupo(user)
            elif command == 'sair':
                print("Desconectando...\n")
                break
            elif command == 'show':
                print(user)

    def singning_up(self):
        """Cria um novo usuário"""
        print("Olá novato!! Vamos fazer seu cadastro")
        login = input("Digite seu login: ")
        nickname = input("Digite seu nickname: ")
        password = input("Digite sua senha: ")
        users.append(User(login, nickname, password))

    def group_creation(self, criador):
        name = input("Forneça o nome do grupo: ")
        new_group = Group(criador, name)
        criador.groups = new_group
        groups.append(new_group)

    def group_session(self, user, group):

        print(f"\nBem vindo a {group.name}, {user.nickname}.")
    
        while True:
            print("\n'add_membro' - para adicionar membro.")
            print("'show', para informacoes do grupo")
            print("'sair' - para sair do grupo.\n")
            
            command = input("comando: ")
            if command == 'add_membro':
                nickname = input("Forneça o nickname do novo membro: ")
                for a_user in users:
                    if a_user.nickname == nickname:
                        group.add_membro(user, a_user)
            elif command == 'show':
                group.show()
            elif command == 'sair':
                print("Saindo do grupo...")
                break
        
    def entrar_grupo(self, user):
        if user.groups:
            print(f"\nOlá {user.nickname}")
            print("Você tem acesso a tais grupos:")
            for group in user.groups:
                print(f"     {group.name}")
            print("")
            
            name = input("Forneça o nome do grupo em que deseja entrar: ")
            for group in groups:
                if group.name == name:
                    print(f"Entrando no grupo {name}")
                    self.group_session(user, group)
        
    def singning_in(self):
        login = input("Digite seu login: ")
        password = input("Digite sua senha: ")

        for user in users:
            if user.login == login and user.password == password:
                self.session_init(user)

    def majority_verification(self):
        print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
        print("'sim' - caso tenha idade maior ou igual a 18 anos.")
        print("'nao' - caso seja menor de idade.\n")
        return input("Resposta: ")

    def show(self):
        print("***Users Info***")
        for ouser in self.users.values():
            print(f"    login: {ouser.login}\n    nickname: {ouser.nickname}\n    password: {ouser.password}\n") 

    def exit(self):
        exit()

    


    