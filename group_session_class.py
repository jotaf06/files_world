from find_user_bynick_class import FindUser

class GroupSession():
    def __init__(self, users, group, user):
        self.users = users
        self.group = group
        self.user = user

    def add_membro(self):
        """Adiciona um membro"""
        if self.user not in self.group.admins:
            print("Você não tem permissão para realizar essa operação...")
        else:
            print("\nOlá admin")
            
            nickname = input("Quem você deseja adicionar no seu grupo?: ")
            ouser = FindUser().find(self.users, nickname)
            if ouser == None:
                print("Usuário não encontrado!")
                return None
            
            self.group.membros.append(ouser)
            ouser.groups.append(self.group)
            
            acces_level = input("Deseja dar nível de acesso admin? (S ou N): ")
            if acces_level == "S":
                self.group.admins.append(ouser)
            print("Operação bem sucedida.")
    
    def session(self):
        print(f"\nBem vindo a {self.group.name}, {self.user.nickname}.")

        while True:
            print("\n'add_membro' - para adicionar membro.")
            print("'show', para informacoes do grupo")
            print("'sair' - para sair do grupo.\n")
            
            command = input("comando: ")
            if command == 'add_membro':
                self.add_membro()

            elif command == 'show':
                self.group.show()

            elif command == 'sair':
                print("Saindo do grupo...")
                break

    
