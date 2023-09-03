class Group():
    def __init__(self, criador, name):
        self.criador = criador
        self.__membros = [criador]
        self.__admins = [criador]
        self.__name = name
    
    @property
    def membros(self):
        return self.__membros
    
    @membros.setter
    def membros(self, new_membro):
        self.__membros.append(new_membro)

    @property
    def admins(self):
        return self.__admins
    
    @admins.setter
    def admins(self, new_admin):
        self.__admins.append(new_admin)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def add_membro(self, user, a_user):
        """Adiciona um membro"""
        if user not in self.admins:
            print("Você não tem permissão para realizar essa operação...")
        else:
            print("\nOlá admin")
            
            self.membros = a_user
            a_user.groups = self
            
            acces_level = input("Deseja dar nível de acesso admin? (S ou N): ")
            if acces_level == "S":
                self.admins = a_user
            print("Operação bem sucedida.")

    def show(self):
        print("\nGroup")
        print(f"Criador: {self.criador.nickname}")
        print("")
        
        print(f"Membros: ")
        for user in self.membros:
            print(f"    {user.nickname}", end=" ")
        print("")

        print("Admins:")
        for user in self.admins:
            print(f"    {user.nickname}", end=" ")
        print("")
        print(f"Group name:\n   {self.name}")