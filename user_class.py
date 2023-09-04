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
        return

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
    def privacity(self, new_password):
        self.__password = new_password

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
        self.__groups.append(new_group)
    
    def edition_commands(self):
        print("\n'comandos' - mostra as opções de edição.")
        print("'login' - altera seu login.")
        print("'nickname' - altera o nickname")
        print("'senha' - muda a senha")
        print("'editar_privacidade' bloqueia/desbloqueia o acesso às suas informações.")
        print("'delecao_de_conta' - apaga o usuário e todo conteúdo associado a ele da rede.")
        print("'sair' - sair do modo de edição.\n")

    def edit_login(self, users):
        new_login = input("Digite se novo login")
        while True:
            for user in users:
                if user.login == new_login:
                    print("Login inválido!!")
                    new_login = input("Digite um novo login")
            print("Login válido")
            self.login = new_login
            return
            
    def edit_nickname(self, users):
        new_nickname = input("Digite se novo nickname")
        while True:
            for user in users:
                if user.nickname == new_nickname:
                    print("Nickname inválido!!")
                    new_nickname = input("Digite um novo Nickname")
            print("Nickname válido")
            self.nickname = new_nickname
            return

    def edit_password(self):
        old_password = input("Antiga senha: ")
        
        if old_password == self.password:
            self.password = input("Nova senha: ")
            print("Operação bem sucedida")
            return
        else:
            print("Senha incorreta. Não foi possível fazer a operação")

    def edit_privacity(self):
        """Torna o acesso as informações do usuário restrito"""
        if self.privacity == 0:
            print("\nSeu usuário tem o perfil aberto.")
        elif self.privacity == 1:
            print("\nSeu usuário tem o perfil fechado.")

        print("'privado' - mantem ou torna privado.")
        print("'aberto' - mantem ou torna aberto.\n")

        command = input("comando_de_privacidade: ")

        if command == 'privado':
            self.privacity = 1
        elif command == 'aberto':
            self.privacity = 0
        return

    def del_user(self, users):
        """Deleta um usuario da rede"""
        print("\nTem certeza que deseja deletar seu usuario?\n")
        print("'del' - para deletar")
        print("'cancelar' - cancelar delecao de usuario,\n")

        command = input("commando_de_delecao: ")
        if command == 'del':
            users.remove(self)
            print("Delecao de usuário realizada com sucesso.")
            exit()
        elif command == 'cancelar':
            print("Operação abordada...\n")
            return

    def add_amigo(self, a_user):
        try:
            if a_user not in self.friends:
                self.friends = a_user
                print("Amigo adicionado!!\n")
                for user in self.friends:
                    print(f"{user.nickname}", sep="     ")
                return 
            elif a_user == None:
                raise ValueError("Esse usuário não existe.")
            else:
                print("Esse usuário já é seu amigo.")
        except ValueError as e:
            print(e)
        
    def acessing(self, a_user, manager):
        if self in a_user.friends:
            manager.acessing(self, a_user)
        else:
            print("Você não tem acesso a esse perfil")
            
    def non_existing_user(self):
        print("Usuário inexistente. Esse login não está cadastrado na rede.")
        print("Abordando operação sing_in...\n")
        return None
        
    def __str__(self):
        string = f"    login: {self.login}\n"
        string += f"    nickname: {self.nickname}\n"
        string += f"    senha: {self.password}\n"
        string += f"    privacidade: {self.privacity}\n"
        return string

class SuperUser(User):
    def __init__(self, login, nickname, password):
        super().__init__(login, nickname, password)

    def acessing(self, a_user, manager):
        manager.acessing(self, a_user)
