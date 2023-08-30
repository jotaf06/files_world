from files_world import FilesWorld

ofilesworld = FilesWorld()

print("BEM VINDO A REDE FilesWorld!\n")
print("ATENÇÃO: Os comandos da rede devem ser fornecidos exatamente como forem apresentados.")

while True:

    print("\n'sing_in' - entrar na rede, caso ja possua um usuário.")
    print("'sing_up' - cadastra um usuário.")
    print("'exit' - Desliga a aplicação.\n")
    command = input("Digite um comando: \n")

    if command == 'sing_in':
        ofilesworld.singning_in()
    elif command == 'sing_up':
        try:
            o_user = ofilesworld.singning_up()
            ofilesworld.users = o_user
        except Exception as e:
            print(e)
    elif command == 'exit':
        ofilesworld.exit()
    elif command == 'show':
        ofilesworld.show()