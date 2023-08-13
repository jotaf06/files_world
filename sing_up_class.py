from user_info_generator_class import UserInfoGenerator

class SingUp():
    def __init__(self, users):
        self.users = users

    def singning_up(self):
        """Cria um novo usuário"""
        print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
        print("'sim' - caso tenha idade maior ou igual a 18 anos.")
        print("'nao' - caso seja menor de idade.\n")
        answer = input("Resposta: ")

        if answer == 'nao':
            print("Você não tem idade suficiente para ser um usuário dessa rede.\n\n")
        elif answer == 'sim':
            o_user_info_generator = UserInfoGenerator(self.users)
            return o_user_info_generator.generate_info()

            