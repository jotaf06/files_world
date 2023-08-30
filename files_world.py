from user_class import User
from sing_in_class import SingIn
from session_class import Session
from user_info_generator_class import UserInfoGenerator

class FilesWorld():
    def __init__(self):
        self.__users = {}
        self.__groups = {}

    @property
    def users(self):
        return self.__users
    
    @users.setter
    def users(self, new_user):
        self.__users[new_user.login] = new_user

    @property
    def groups(self):
        return self.__groups
    
    @groups.setter
    def groups(self, new_group):
        self.__groups[new_group.name] = new_group

    def session_init(self, ouser):
        osession = Session(self.users, self.groups, ouser)
        print(f"Olá {ouser.nickname} Você está conectado a rede.")
        print("Digite 'lista_de_comandos' para ver os comandos da rede\n")

        sair_da_rede = False
        while sair_da_rede == False:
                
            command = input("comando : ")
            if command == 'lista_de_comandos':
                osession.commands()
            elif command == 'editar_usuario':
                osession.user.edition_init(self.users)
            elif command == 'acessar_perfil':
                a_user = osession.find_user()
                osession.user.access_perfil(a_user)
            elif command == 'add_amigo':
                a_user = osession.find_user()
                osession.user.add_amigo(a_user)
            elif command == 'subir_arquivo':
                osession.uploading()
            elif command == 'criar_grupo':
                osession.group_creation()
            elif command == 'entrar_grupo':
                osession.entrar_grupo()
            elif command == 'sair':
                sair_da_rede = True
                print("Desconectando...\n")
            elif command == 'show':
                print(self.user)

    def singning_in(self):
        osing_in = SingIn(self.users)
        
        ouser = osing_in.signing_in()
        if ouser:
            self.session_init(ouser)

    def majority_verification(self):
        print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
        print("'sim' - caso tenha idade maior ou igual a 18 anos.")
        print("'nao' - caso seja menor de idade.\n")
        return input("Resposta: ")

    def singning_up(self):
        """Cria um novo usuário"""
        majority = self.majority_verification()
        
        if majority == 'nao':
            raise Exception("Você não tem idade suficiente para ser um usuário dessa rede.\n\n")
        elif majority == 'sim':
            ouser_info_generator = UserInfoGenerator(self.users)
            login, nickname, password = ouser_info_generator.generate_info()
            return User(login, nickname, password)

    def show(self):
        print("***Users Info***")
        for ouser in self.users.values():
            print(f"    login: {ouser.login}\n    nickname: {ouser.nickname}\n    password: {ouser.password}\n") 

    def exit(self):
        exit()

    


    