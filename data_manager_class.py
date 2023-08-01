import json

class DataManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {}

    def save_data(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent='\t')

class GroupsManager(DataManager):
    def __init__(self):
        super().__init__('groups.json')
        self.groups = self.load_data()
    
    def criar_grupo(self, user_nickname):
        """Cria um grupo em que o admim é o usuário de nickname user"""
        while True:
            new_group_name = input("\nNome do grupo: ")
            if new_group_name in self.groups:
                print("Ja existe um grupo com esse nome.")
            else: 
                self.groups[new_group_name] = {'admins' : [user_nickname], 
                                               'users' : [user_nickname]}

                self.save_data(self.groups)
                print(f"\nGrupo criado com sucesso {user_nickname}.")
                break

    def add_membro(self, user_nickname, group_name):
        """Adiciona um membro"""
        if user_nickname not in self.groups[group_name]['admins']:
            print("Você não tem permissão para realizar essa operação...")
        else:
            print("\nOlá admin")
            new_member_nickname = input("Quem você deseja adicionar no seu grupo?: ")
            acces_level = input("Qual o nível de acesso do usuário? (admin ou user): ")

            if acces_level == "admin":
                self.groups[group_name]['admins'].append(new_member_nickname)
            else:
                self.groups[group_name]['users'].append(new_member_nickname)

            self.save_data(self.groups)
            print("Operação bem sucedida.")

    def eh_membro(self, user_nickname, group):
        """Verifica se um usuario eh membro de certo grupo"""
        users = group['users']
        for user in users:
            if user == user_nickname:
                return user
        return None

    def entrar_grupo(self, users, user_login, groups):
        """Aqui acontece a interação do usuario com o grupo"""
        group_name = input("\nGrupo que se deseja entrar: ")

        if group_name not in groups:
            print("Esse grupo não existe.")
        else:
            group = groups[group_name]
            user_nickname = users[user_login]['nickname']
            user_membro = self.eh_membro(user_nickname, group)
            if user_membro != None:
                print(f"\nBem vindo a {group_name}, {user_nickname}.")
                
                while True:
                    print("\n'add_membro' - para adicionar membro.")
                    print("'sair' - para sair do grupo.\n")
                    
                    command = input("comando: ")
                    if command == 'add_membro':
                        self.add_membro(user_membro, group_name)

                    elif command == 'sair':
                        print("Saindo do grupo...")
                        break
            else:
                print("Você não é membro desse grupo!")

class FriendshipManager(DataManager):
    def __init__(self):
        super().__init__('amigos.json')
    
    def adiciona_amigo(self, user_login, friendships):
        new_friend_nickname = input("\nQual o nickname do seu novo amigo?: ")
        
        if user_login not in friendships:
            friendships[user_login] = [new_friend_nickname]
        else:
            friendships[user_login].append(new_friend_nickname)
        print("Amigo adicionado!!\n")