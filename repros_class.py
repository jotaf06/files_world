
from user_manager_class import UsersManager

class RePros:
    def __init__(self):
        self.users_manager = UsersManager()

    def run(self):
        print("BEM VINDO A REDE RePros!\n")
        print("ATENÇÃO: Os comandos da rede devem ser fornecidos exatamente como forem apresentados.")

        users = self.users_manager.load_data()
        exit = False
        while not exit:

            print("\n'sing_in' - entrar na rede, caso ja possua um usuário.")
            print("'sing_up' - cadastra um usuário.")
            print("'exit' - Desliga a aplicação.\n")
            command = input("Digite um comando: \n")

            if command == 'sing_in':
                input_login = input("login: ")
                input_password = input("senha: ")

                if input_login not in users:
                    print("Usuário inexistente. Esse login não está cadastrado na rede.")
                    print("Abordando operação sing_in...\n")
                else:
                    if users[input_login]['password'] != input_password:
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
                    create_new_user(self.users)
                
                elif age == 'nao':
                    print("Você não tem idade suficiente para ser um usuário dessa rede.\n\n")
            
            elif command == 'exit':
                exit = True

if __name__ == "__main__":
    rede_repros = RePros()
    rede_repros.run()