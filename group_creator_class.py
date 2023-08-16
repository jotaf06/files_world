from group_finder_byname_class import GroupFinder
from group_class import Group

class GrupoCreator():
    def creation(self, groups, user):
        """Cria um grupo em que o admim é o usuário de nickname user"""
        while True:
            name = input("\nNome do grupo: ")
            group = GroupFinder().find(groups, name)
            if group:
                    print("Ja existe um grupo com esse nome.")
            else: 
                new_group = Group(user, name)
                user.groups.append(new_group)
                groups[name] = new_group
                print(f"\nGrupo criado com sucesso {user.nickname}.")
                break