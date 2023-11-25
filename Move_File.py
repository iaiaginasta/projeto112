import os
import shutil


from_dir  = "C:/Users/Eleven/OneDrive/Documentos/Byju's/python/projeto 111"
to_dir  ="C:/Users/Eleven/OneDrive/Área de Trabalho"

list_of_files = os.listdir(from_dir )

for file_name in list_of_files:
    raiz, ext = os.path.splitext(file_name)
    if ext == "":
        continue 
    if ext in ['.jpg', '.jpeg', '.png', '.jfif', '.gif']:
        path1 = from_dir  + '/' + file_name
        path2 = to_dir 
        path3 = to_dir  + '/' + file_name

        if os.path.exists(path2):
            print("movendo...")
            shutil.move(path1, path3)
        else:
            print("criando a pasta...")
            os.makedirs(path2)
            shutil.move(path1, path3)



