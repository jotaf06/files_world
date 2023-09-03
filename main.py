from files_world import FilesWorld

ofilesworld = FilesWorld()
# atributos são usuários e grupos

print("BEM VINDO A REDE FilesWorld!\n")
print("ATENÇÃO: Os comandos da rede devem ser fornecidos exatamente como forem apresentados.")

def majority_verification():
    print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
    print("'sim' - caso tenha idade maior ou igual a 18 anos.")
    print("'nao' - caso seja menor de idade.\n")
    return input("Resposta: ")

if (majority_verification() == "sim"):
    while True:
        print("\n'sing_in' - entrar na rede, caso ja possua um usuário.")
        print("'sing_up' - cadastra um usuário.")
        print("'exit' - Desliga a aplicação.\n")
        command = input("Digite um comando: \n")

        if command == 'sing_in':
            ofilesworld.singning_in()
        elif command == 'sing_up':
            ofilesworld.singning_up()
        elif command == 'exit':
            ofilesworld.exit()
        elif command == 'show':
            ofilesworld.show()
else:
    print("Você não tem idade suficiente para fazer uso da rede")