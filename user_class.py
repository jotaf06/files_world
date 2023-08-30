from user_editor_class import UserEditor
from perfil_files_manager_class import PerfilFilesManager

class User():
    def __init__(self, login, nickname, password):
        self.__login = login
        self.__nickname = nickname
        self.__password = password
        self.__privacity = 0
        self.__friends = []
        self.__groups = []
    
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        self.__login = new_login

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, new_nickname):
        self.__nickname = new_nickname

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def privacity(self):
        return self.__privacity
    
    @privacity.setter
    def privacity(self, new_privacity):
        self.__privacity = new_privacity
    
    @property
    def friends(self):
        return self.__friends

    @friends.setter
    def friends(self, new_friend):
        self.__friends.append(new_friend)

    @property
    def groups(self):
        return self.__groups

    @groups.setter
    def groups(self, new_group):
        self.__groups = new_group

    def edition_init(self):
        ouser_editor = UserEditor(self.users, self)
    
        print("Você está na área de edição das informações de seu usuário\n")
        print("Digite 'comandos' para ver os comandos de edição")

        sair_modo_edicao = False
        while sair_modo_edicao == False:

            command = input("comando: ")
            if command == 'comandos':
                ouser_editor.commands()
            elif command == 'login':
                self.user.login = ouser_editor.edit_login()
            elif command == 'nickname':
                self.user.nickname = ouser_editor.edit_nickname()
            elif command == 'senha':
                self.user.password = ouser_editor.edit_password()
            elif command == 'editar_privacidade':
                ouser_editor.edit_privacity()
            elif command == 'delecao_de_conta':
                ouser_editor.del_user()
            elif command == 'sair':
                ouser_editor.final_state()
                sair_modo_edicao = True


    def access_perfil(self, a_user):
        operfil_files_manager = PerfilFilesManager()
        access = operfil_files_manager.access_verification(self, a_user)
        if access:
            operfil_files_manager.acessing(a_user)

    def add_amigo(self, a_user):
        try:
            if a_user not in self.friends:
                self.friends = a_user
                print("Amigo adicionado!!\n")
            elif a_user == None:
                raise ValueError("Esse usuário não existe.")
            else:
                print("Esse usuário já é seu amigo.")
        except ValueError as e:
            print(e)
        
    def __str__(self):
        return f"***Debug***\n    login: {self.login}\n   nickname: {self.nickname}\n    password: {self.password}\n      privacity: {self.privacity}\n    friends: {self.friends}\n    groups: {self.groups}"
        
