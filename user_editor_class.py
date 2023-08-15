from user_editor_commands_class import UserEditorCommands
from user_info_generator_class import UserInfoGenerator
from user_editor_privacity_class import UserEditorPrivacity
from user_editor_delector_class import UserEditorDelector

class UserEditor():
    def __init__(self, users, user):
        self.users = users
        self.user = user
    
    def editor(self):
        print("Você está na área de edição das informações de seu usuário\n")
        print("Digite 'comandos' para ver os comandos de edição")

        sair_modo_edicao = False
        while sair_modo_edicao == False:

            command = input("comando: ")
            if command == 'comandos':
                UserEditorCommands().commands()
            elif command == 'login':
                self.user.login = UserInfoGenerator(self.users).new_login()
            elif command == 'nickname':
                self.user.nickname = UserInfoGenerator(self.user).new_nickname()
            elif command == 'senha':
                self.user.senha = UserInfoGenerator(self.users).new_password()
            elif command == 'editar_privacidade':
                UserEditorPrivacity().edition(self.user)
            elif command == 'delecao_de_conta':
                UserEditorDelector().delection(self.users, self.user)
            elif command == 'sair':
                print("***Estado Final Da Edição***")
                print(f"    login: {self.user.login}")
                print(f"    nickname: {self.user.nickname}")
                print(f"    senha: {self.user.senha}")
                print("Saindo da área de edição...\n")
                sair_modo_edicao = True
