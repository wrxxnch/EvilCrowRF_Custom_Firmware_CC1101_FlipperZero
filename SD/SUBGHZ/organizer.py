import os
import shutil

# Caminho base (onde está a pasta SUBGHZ)
BASE = os.path.abspath(os.path.dirname(__file__))

for root, dirs, files in os.walk(BASE, topdown=False):
    for file in files:
        if file.lower().endswith(".sub"):
            full_path = os.path.join(root, file)

            # Caminho relativo a partir de SUBGHZ
            rel_path = os.path.relpath(root, BASE)

            # Divide pastas e ignora a primeira (ex: Vehicles)
            parts = rel_path.split(os.sep)
            if len(parts) > 1:
                parts = parts[1:]  # remove a primeira
            else:
                parts = parts

            # Junta as pastas em um só nome
            new_folder_name = "".join(parts)

            # Novo diretório dentro de SUBGHZ
            new_dir = os.path.join(BASE, new_folder_name)
            os.makedirs(new_dir, exist_ok=True)

            # Novo caminho do arquivo
            new_file_path = os.path.join(new_dir, file)

            print(f"Movendo: {full_path} -> {new_file_path}")
            shutil.move(full_path, new_file_path)

# Depois de mover, remover pastas vazias
for root, dirs, files in os.walk(BASE, topdown=False):
    if root == BASE:
        continue
    if not os.listdir(root):
        print(f"Removendo pasta vazia: {root}")
        os.rmdir(root)

print("Organização concluída!")
