
from user_manager_class import UsersManager
from singning_up_class import SingInUP

class FilesWorld:
    def __init__(self):
        self.users_manager = UsersManager()
        self.users = self.users_manager.load_data()

    def run(self):
        print("BEM VINDO A REDE RePros!\n")
        print("ATENÇÃO: Os comandos da rede devem ser fornecidos exatamente como forem apresentados.")

        exit = False
        while not exit:

            print("\n'sing_in' - entrar na rede, caso ja possua um usuário.")
            print("'sing_up' - cadastra um usuário.")
            print("'exit' - Desliga a aplicação.\n")
            command = input("Digite um comando: \n")

            if command == 'sing_in':
                input_login = input("login: ")
                input_password = input("senha: ")

                if input_login not in self.users:
                    print("Usuário inexistente. Esse login não está cadastrado na rede.")
                    print("Abordando operação sing_in...\n")
                else:
                    if self.users[input_login]['password'] != input_password:
                        print("Senha inválida!!!\n")
                    else:            
                        print("sing_in realizado com sucesso, entrando na rede RePros...\n")
                        self.users_manager.entrando_na_rede(input_login)
            
            elif command == 'sing_up':
                print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
                print("'sim' - caso tenha idade maior ou igual a 18 anos.")
                print("'nao' - caso seja menor de idade.\n")
                age = input("Resposta: ")

                if age == 'sim':
                    singup_manager = SingInUP()
                    singup_manager.create_new_user(self.users_manager.users)
                    self.users_manager.save_data(self.users_manager.users)
                    self.users = self.users_manager.load_data()
                
                elif age == 'nao':
                    print("Você não tem idade suficiente para ser um usuário dessa rede.\n\n")
            
            elif command == 'exit':
                exit = True

if __name__ == "__main__":
    rede_repros = FilesWorld()
    rede_repros.run()