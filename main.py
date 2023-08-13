from files_world import FilesWorld

ofilesworld = FilesWorld()

print("BEM VINDO A REDE RePros!\n")
print("ATENÇÃO: Os comandos da rede devem ser fornecidos exatamente como forem apresentados.")

exit = False
while not exit:

    print("\n'sing_in' - entrar na rede, caso ja possua um usuário.")
    print("'sing_up' - cadastra um usuário.")
    print("'exit' - Desliga a aplicação.\n")
    command = input("Digite um comando: \n")

    if command == 'sing_in':
        pass
    elif command == 'sing_up':
        ofilesworld.singning_up()
    elif command == 'show':
        ofilesworld.show()
    elif command == 'exit':
        exit = True