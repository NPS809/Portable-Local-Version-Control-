# Рядом с этим файлом должно быть две папки: Code и Versions

import shutil
import os

path = os.path.dirname(__file__)

code_path = path + "\\Code\\"
vers_path = path + "\\Versions\\"

print("Получение исходного кода...\n")
files_and_dirs = os.listdir(code_path)
if len(files_and_dirs) == 0:
    input("Увы, но в папке Code ничего нет...\n")
    exit()

upd_name = upd_desc = ""
version = input("Введите версию проекта (Пример: 1.0.0): ")
if input("\nДобавить информацию info.txt? y/n: ").strip().lower() == "y":
    upd_name = input("\nВведите название обновления: ")
    upd_desc = input("\nОпишите нововведения: ")

new_dir_path = f"{vers_path}v{version}\\"
os.mkdir(new_dir_path)

for name in files_and_dirs:
    shutil.copytree(code_path, new_dir_path, dirs_exist_ok=True)

if upd_name != "" or upd_desc != "":
    with open(f"{new_dir_path}info.md", "x", encoding="utf-8") as file:
        file.write(f"{upd_name}\n")
        file.write(f"Version: {version}\n\n")
        file.write(upd_desc)

input("Для завершения операции нажмите Enter ↵")
