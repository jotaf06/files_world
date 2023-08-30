from user_info_generator_class import UserInfoGenerator

class UserEditor():
    def __init__(self, users, user):
        self.users = users
        self.user = user
        self.info_generator = UserInfoGenerator(self.users)

    def commands(self):
        print("\n'comandos' - mostra as opções de edição.")
        print("'login' - altera seu login.")
        print("'nickname' - altera o nickname")
        print("'senha' - muda a senha")
        print("'editar_privacidade' bloqueia/desbloqueia o acesso às suas informações.")
        print("'delecao_de_conta' - apaga o usuário e todo conteúdo associado a ele da rede.")
        print("'sair' - sair do modo de edição.\n")
    
    def edit_login(self):
        return self.info_generator.new_login()

    def edit_nickname(self):
        return self.info_generator.new_nickname()

    def edit_password(self):
        return self.info_generator.new_password()

    def edit_privacity(self):
        """Torna o acesso as informações do usuário restrito"""
        if self.user.privacity == 0:
            print("\nSeu usuário tem o perfil aberto.")

        elif self.user.privacity == 1:
            print("\nSeu usuário tem o perfil fechado.")

        print("'privado' - mantem ou torna privado.")
        print("'aberto' - mantem ou torna aberto.\n")

        command = input("comando_de_privacidade: ")

        if command == 'privado':
            self.user.privacity = 1
        elif command == 'aberto':
            self.user.privacity = 0

    def del_user(self):
        """Deleta um usuario da rede"""
        print("\nTem certeza que deseja deletar seu usuario?\n")
        print("'del' - para deletar")
        print("'cancelar' - cancelar delecao de usuario,\n")

        command = input("commando_de_delecao: ")
        if command == 'del':
            del self.users[self.user.login]
            print("Delecao de usuário realizada com sucesso.")
            exit()
        elif command == 'cancelar':
            print("Operação abordada...\n")

    def final_state(self):
        print("***Estado Final Da Edição***")
        print(f"    login: {self.user.login}")
        print(f"    nickname: {self.user.nickname}")
        print(f"    senha: {self.user.password}")
        print(f"    privacidade: {self.user.privacity}")
        print("Saindo da área de edição...\n")
