class Group():
    def __init__(self, criador, name):
        self.criador = criador
        self.membros = [criador]
        self.admins = [criador]
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def add_membro(self, a_user):
        """Adiciona um membro"""
        if self.user not in self.group.admins:
            print("Você não tem permissão para realizar essa operação...")
        else:
            print("\nOlá admin")
            if a_user == None:
                print("Usuário não encontrado!")
                return None
        
            self.membros.append(a_user)
            a_user.groups = self.group
            
            acces_level = input("Deseja dar nível de acesso admin? (S ou N): ")
            if acces_level == "S":
                self.admins.append(a_user)
            print("Operação bem sucedida.")

    def show(self):
        print("GroupDebug")
        print(f"    criador: {self.criador}")
        print(f"    membros: {self.membros}")
        print(f"    admins: {self.admins}")
        print(f"    name: {self.name}")