from user_class import User
from sing_up_class import SingUp
from sing_in_class import SingIn
from navigation_class import Navigation

class FilesWorld():
    def __init__(self):
        self.users = {}
        self.groups = {}

    def show(self):
        print("***Users Info***")
        for ouser in self.users.values():
            print(f"    login: {ouser.login}\n    nickname: {ouser.nickname}\n    password: {ouser.password}\n") 

    def singning_up(self):
        login, nickname, password = SingUp(self.users).singning_up()
        self.users[login] = User(login, nickname, password)

    def singning_in(self):
        SingIn().signing_in()
    
    def navigation(self):

    


    