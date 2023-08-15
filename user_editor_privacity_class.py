class UserEditorPrivacity():
    def edition(self, user):
        """Torna o acesso as informações do usuário restrito"""
        if user.privacity == 0:
            print("\nSeu usuário tem o perfil aberto.")

        elif user.privacity == 1:
            print("\nSeu usuário tem o perfil fechado.")

        print("'privado' - mantem ou torna privado.")
        print("'aberto' - mantem ou torna aberto.\n")

        command = input("comando_de_privacidade: ")

        if command == 'privado':
            user.privacity = 1
        elif command == 'aberto':
            user.privacity = 0