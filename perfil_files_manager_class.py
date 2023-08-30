from finder_class import FindUser
import os

class PerfilFilesManager():
    def __init__(self):
        pass

    def access_verification(self, user, a_user):
        """faz a validação de acesso a um perfil"""
        if a_user == None:
            print("\nNão há usuário com esse perfil.")
            return False
        
        elif a_user.privacity == 1:
            print("\nEsse perfil é privado.")
            if user in a_user.friends:
                return True
            else:
                print("Você não tem acesso a esse perfil.")
                return False
    
        elif a_user.privacity == 0:
            print("\nEsse perfil é aberto.")
            return True

    def acessing(self, a_user):
        perfil_dir = os.path.join('files_world2', a_user.nickname)
        print(perfil_dir)
        
        if not os.path.exists(perfil_dir):
            print("\nNão há arquivos no perfil.")
        else:
            files = os.listdir(perfil_dir)
            if len(files) == 0:
                print("Não há arquivos no perfil.")
            else:
                print("Arquivos no perfil:")
                for file in files:
                    print(file)

    def uploading(self, nickname):
        """Faz upload de arquivo no perfil"""
        file_path = input("Forneça o caminho do arquivo: ")
        
        if not os.path.exists(file_path):
            print('Arquivo não encontrado.')
            return None

        # Diretório de destino para salvar os arquivos
        upload_dir = os.path.join('files_world2', nickname)

        # Criar o diretório de upload se não existir
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Obter o nome do arquivo
        file_name = os.path.basename(file_path)

        # Caminho de destino do arquivo
        destination_path = os.path.join(upload_dir, file_name)

        # Copiar o arquivo para o diretório de upload
        with open(file_path, 'rb') as src_file, open(destination_path, 'wb') as dest_file:
            dest_file.write(src_file.read())

        # Salvar informações do arquivo
        file_info = {
            'file_name': file_name,
            'file_path': destination_path,
            'uploaded_by': nickname
        }
        print(file_info)
