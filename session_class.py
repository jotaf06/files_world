from user_editor_class import UserEditor
from perfil_access_class import PerfilAccess
from perfil_files_manager_class import PerfilFilesManager
from find_user_bynick_class import FindUser
from group_creator_class import GrupoCreator
from group_finder_byname_class import GroupFinder
from group_session_class import GroupSession


class Session():
    def __init__(self, users, groups, user):
        self.users = users
        self.groups = groups
        self.user = user

    def commands(self):
        print("'editar_usuario' - edita as informações associadas a um usuário.")
        print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
        print("'add_amigo' - adiciona um amigo.")
        print("'subir_arquivo' - subir conteúdo no perfil.")
        print("'criar_grupo' - cria um grupo.")
        print("'entrar_grupo' - entrar em um grupo.")
        print("'sair' - para se desconectar.\n")

    def find(self, nickname):
        FindUser(self.users, nickname).find()

    def session(self):
        print(f"Olá {self.user.nickname} Você está conectado a rede.")
        print("Digite 'lista_de_comandos' para ver os comandos da rede\n")

        sair_da_rede = False
        while sair_da_rede == False:

            command = input("comando : ")
            if command == 'lista_de_comandos':
                self.commands()

            elif command == 'editar_usuario':
                UserEditor(self.users, self.user).editor()

            elif command == 'acessar_perfil':
                continuar = 1
                while continuar:
                    a_user = PerfilAccess().access(self.users, self.user)
                    if a_user:
                        PerfilFilesManager().acessing(a_user)
                    continuar = int(input("\nDigite '1' para continuar ou '0' para parar a operação: "))
                    
            elif command == 'add_amigo':
                nickname = input("\nQual o nickname do seu novo amigo?: ")
                ouser = self.find(nickname)
                if ouser:
                    self.user.friends.append(ouser)
                    print("Amigo adicionado!!\n")

            elif command == 'subir_arquivo':
                PerfilFilesManager().uploading(self.user.nickname)
                
            elif command == 'criar_grupo':
                GrupoCreator().creation(self.groups, self.user)

            elif command == 'entrar_grupo':
                name = input("\nNome do grupo em que se deseja entrar: ")
                group = GroupFinder().find(self.groups, name)
                if group == None:
                    print("Esse grupo não existe")
                else:
                    if group not in self.user.groups:
                        print("Você não eh membro do grupo.")
                    else:
                        GroupSession(self.users, group, self.user).session()

            elif command == 'sair':
                sair_da_rede = True
                print("Desconectando...\n")
            
            elif command == 'show':
                print(self.user)
        