from user_editor_class import UserEditor
from perfil_files_manager_class import PerfilFilesManager

class User():
    def __init__(self, login, nickname, password):
        self.login = login
        self.nickname = nickname
        self.password = password
        self.privacity = 0
        self.friends = []
        self.groups = []
    
    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, new_login):
        self.login = new_login

    @property
    def nickname(self):
        return self.nickname

    @nickname.setter
    def nickname(self, new_nickname):
        self.nickname = new_nickname

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, new_password):
        self.password = new_password

    @property
    def privacity(self):
        return self.privacity
    
    @privacity.setter
    def privacity(self, new_privacity):
        self.privacity = new_privacity
    
    @property
    def friends(self):
        return self.friends

    @friends.setter
    def friends(self, new_friend):
        self.friends.append(new_friend)

    @property
    def groups(self):
        return self.groups

    @groups.setter
    def groups(self, new_groups):
        self.groups = new_groups

    def edit(self, users):
        ouser_editor = UserEditor(users, self)
        ouser_editor.edit()

    def access_perfil(self, a_user):
        operfil_files_manager = PerfilFilesManager(self, a_user)
        access = operfil_files_manager.access_verification()
        if access:
            operfil_files_manager.acessing()

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
        
