import os

# 1. Указать нормализованный абсолютный путь к файлу test_file_1.txt
file_1_path = os.path.abspath('data_path_1/test_file_1.txt')
print("Абсолютный путь к test_file_1.txt:", file_1_path)

# 2. Вывести содержимое папки вашего нового проекта
print("\nСодержимое папки проекта:")
for root, dirs, files in os.walk('.'):
    print(f'Папка: {root}')
    for dir in dirs:
        print(f'  Подпапка: {dir}')
    for file in files:
        print(f'  Файл: {file}')

# 3. Составить нормализованный абсолютный путь к файлу test_file_3.txt
file_3_path = os.path.join(os.path.abspath('data_path_2'), 'test_file_3.txt')
print("\nАбсолютный путь к test_file_3.txt:", file_3_path)

# 4. Создание и удаление папки внутри папки data_path_2
new_folder_path = os.path.join('data_path_2', 'new_folder')

# Создание новой папки
os.makedirs(new_folder_path, exist_ok=True)
print(f"\nСоздана папка: {new_folder_path}")

# Удаление созданной папки
os.rmdir(new_folder_path)
print(f"Удалена папка: {new_folder_path}")