class Group():
    def __init__(self, criador, name):
        self.criador = criador
        self.membros = [criador]
        self.admins = [criador]
        self.name = name
    
    def show(self):
        print("GroupDebug")
        print(f"    criador: {self.criador}")
        print(f"    membros: {self.membros}")
        print(f"    admins: {self.admins}")
        print(f"    name: {self.name}")