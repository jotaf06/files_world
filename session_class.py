from perfil_files_manager_class import PerfilFilesManager
from finder_class import Finder
from group_class import Group

class Session():
    def __init__(self, users, groups, user):
        self.users = users
        self.__groups = groups
        self.__user = user
        self.finder = Finder(self.users, self.groups)

    @property
    def user(self):
        return self.__user
    
    @property
    def groups(self):
        return self.__groups
    
    @groups.setter
    def groups(self, new_group):
        self.__groups[new_group.name] = new_group

    def commands(self):
        print("'editar_usuario' - edita as informações associadas a um usuário.")
        print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
        print("'add_amigo' - adiciona um amigo.")
        print("'subir_arquivo' - subir conteúdo no perfil.")
        print("'criar_grupo' - cria um grupo.")
        print("'entrar_grupo' - entrar em um grupo.")
        print("'sair' - para se desconectar.\n")

    def find_user(self):
        nickname = input("\nForneça o nickname do usuário: ")
        a_user = self.finder.find_user(nickname)
        return a_user
    
    def find_group(self):
        name = input("\nNome do grupo: ")
        group = self.finder.find_group(name)
        return group

    def uploading(self):
        PerfilFilesManager().uploading(self.user.nickname)

    def group_creation(self):
        """Cria um grupo em que o admim é o usuário de nickname user"""
        while True:
            name = input("\nNome do grupo: ")
            group = self.finder.find_group(name)
            if group:
                    print("Ja existe um grupo com esse nome.")
            else: 
                new_group = Group(self.user, name)
                self.user.groups = new_group
                self.groups = new_group
                print(f"\nGrupo criado com sucesso {self.user.nickname}.")
                return

    def entrar_grupo(self):
        try:
            group = self.find_group()
            if group == None:
                raise Exception("Esse grupo não existe\n")
            else:
                if group not in self.user.groups:
                    raise Exception("Você não eh membro desse grupo\n")
                else:
                    self.group_session_init(group)
        except Exception as e:
            print(e)

    def group_session_init(self, group):

        print(f"\nBem vindo a {group.name}, {self.user.nickname}.")
    
        while True:
            print("\n'add_membro' - para adicionar membro.")
            print("'show', para informacoes do grupo")
            print("'sair' - para sair do grupo.\n")
            
            command = input("comando: ")
            if command == 'add_membro':
                a_user = self.find_user()
                group.add_membro(a_user)
            elif command == 'show':
                group.show()
            elif command == 'sair':
                print("Saindo do grupo...")
                break


        