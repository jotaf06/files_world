from singning_up_class import SingInUP
from data_manager_class import DataManager

class UserEditor(DataManager):
    def __init__(self, user_login, users):
        super().__init__('users.json')
        self.user_login = user_login
        self.users = users

    def privacity_edit(self):
        """Torna o acesso as informações do usuário restrito"""
        user = self.users[self.user_login]
        if user['privacity'] == 0:
            print("\nSeu usuário tem o perfil aberto.")

        elif user['privacity'] == 1:
            print("\nSeu usuário tem o perfil fechado.")

        print("'privado' - mantem ou torna privado.")
        print("'aberto' - mantem ou torna aberto.\n")

        command = input("comando_de_privacidade: ")

        if command == 'privado':
            user['privacity'] = 1
        elif command == 'aberto':
            user['privacity'] = 0

    def remove_user(self):
        """Deleta um usuario da rede"""
        print("\nTem certeza que deseja deletar seu usuario?\n")
        print("'del' - para deletar")
        print("'cancelar' - cancelar delecao de usuario,\n")

        command = input("commando_de_delecao: ")
        if command == 'del':
            del self.users[self.user_login]
            return True
        elif command == 'cancelar':
            print("Operação abordada...\n")
            return False
            
    def edit_user(self):
        """Edita as informações do usuário"""
        print("\n'opts' - mostra as opções de edição.")
        print("'login' - altera seu login.")
        print("'nickname' - altera o nickname")
        print("'senha' - muda a senha")
        print("'editar_privacidade' bloqueia/desbloqueia o acesso às suas informações.")
        print("'delecao_de_conta' - apaga o usuário e todo conteúdo associado a ele da rede.")
        print("'sair' - sair do modo de edição.\n")
        while True:
            command = input("comando de edição: ")
            if command == 'opts':
                self.print_edit_options()
            elif command == 'login':
                self.change_login()
            elif command == 'nickname':
                self.change_nickname()
            elif command == 'senha':
                self.change_password()
            elif command == 'editar_privacidade':
                self.privacity_edit()
            elif command == 'delecao_de_conta':
                remocao = self.remove_user()
                if remocao:
                    self.save_data(self.users)
                    print("Usuário removido, saindo da aplicação.")
                    exit()
            elif command == 'sair':
                print(self.user_login, ":", self.users[self.user_login], "\nEncerrando operação de edição...\n")
                break

    def print_edit_options(self):
        """Exibe as opções de edição"""
        print("\n'opts' - mostra as opções de edição.")
        print("'login' - altera seu login.")
        print("'nickname' - altera o nickname")
        print("'senha' - muda a senha")
        print("'editar_privacidade' bloqueia/desbloqueia o acesso às suas informações.")
        print("'delecao_de_conta' - apaga o usuário e todo conteúdo associado a ele da rede.")
        print("'sair' - sair do modo de edição.\n")

    def change_login(self):
        """Altera o login do usuário"""
        sing_up = SingInUP()
        new_login = sing_up.new_login_user(self.users)
        self.users[new_login] = self.users[self.user_login]
        del self.users[self.user_login]
        self.user_login = new_login

    def change_nickname(self):
        """Altera o nickname do usuário"""
        sing_up = SingInUP()
        user = self.users[self.user_login]
        user['nickname'] = sing_up.new_nickname_user(self.users)

    def change_password(self):
        """Altera a senha do usuário"""
        user = self.users[self.user_login]
        user['password'] = input("Digite sua nova senha: ")
        print("Senha alterada com sucesso!!\n")