class UserEditorDelector():
    def delection(self, users, user):
        """Deleta um usuario da rede"""
        print("\nTem certeza que deseja deletar seu usuario?\n")
        print("'del' - para deletar")
        print("'cancelar' - cancelar delecao de usuario,\n")

        command = input("commando_de_delecao: ")
        if command == 'del':
            del users[user.login]
            print("Delecao de usuário realizada com sucesso.")
            exit()
        elif command == 'cancelar':
            print("Operação abordada...\n")
