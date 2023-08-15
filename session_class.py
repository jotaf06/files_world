from session_command_class import SessionCommand
from user_editor_class import UserEditor
from perfil_access_class import PerfilAccess
from perfil_files_manager_class import PerfilFilesManager

class Session():
    def __init__(self, users, groups, user):
        self.users = users
        self.groups = groups
        self.user = user

    def session(self):
        print(f"Olá {self.user.nickname} Você está conectado a rede.")
        print("Digite 'lista_de_comandos' para ver os comandos da rede\n")

        sair_da_rede = False
        while sair_da_rede == False:

            command = input("comando : ")
            if command == 'lista_de_comandos':
                SessionCommand().commands()

            elif command == 'editar_usuario':
                UserEditor(self.users, self.user).editor()

            elif command == 'acessar_perfil':
                continuar = True
                while continuar:
                    a_user = PerfilAccess().access(self.users, self.user)
                    if a_user:
                        PerfilFilesManager().acessing(a_user)
                    continuar = input("\nDigite 'True' para continuar ou 'False' para parar a operação: ")
                    
            elif command == 'add_amigo':
                nickname = input("\nQual o nickname do seu novo amigo?: ")
                self.user.friends.append(nickname)
                print("Amigo adicionado!!\n")

            elif command == 'subir_arquivo':
                PerfilFilesManager().uploading(self.user.nickname)
                
            elif command == 'criar_grupo':
                pass
            elif command == 'entrar_grupo':
                pass
            elif command == 'sair':
                sair_da_rede = True
                print("Desconectando...\n")