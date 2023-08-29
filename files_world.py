from user_class import User
from sing_in_class import SingIn
from session_class import Session
from user_info_generator_class import UserInfoGenerator

class FilesWorld():
    def __init__(self):
        self.users = {}
        self.groups = {} 

    def singning_in(self):
        osing_in = SingIn(self.users)
        
        ouser = osing_in.signing_in()
        if ouser:
            osession = Session(self.users, self.groups, ouser)
            osession.session()

    def majority_verification(self):
        print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
        print("'sim' - caso tenha idade maior ou igual a 18 anos.")
        print("'nao' - caso seja menor de idade.\n")
        return input("Resposta: ")

    def singning_up(self):
        """Cria um novo usuário"""
        majority = self.majority_verification()
        
        if majority == 'nao':
            print("Você não tem idade suficiente para ser um usuário dessa rede.\n\n")
        elif majority == 'sim':
            login, nickname, password = UserInfoGenerator(self.users).generate_info()
            ouser = User(login, nickname, password)
            self.users[login] = ouser

    def show(self):
        print("***Users Info***")
        for ouser in self.users.values():
            print(f"    login: {ouser.login}\n    nickname: {ouser.nickname}\n    password: {ouser.password}\n") 

    def exit(self):
        exit()

    


    