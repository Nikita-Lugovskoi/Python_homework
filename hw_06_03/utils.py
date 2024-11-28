import json
import os

# Функция для создания папки, если она не существует
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Папка '{directory}' была создана.")
    else:
        print(f"Папка '{directory}' уже существует.")

# Функция для загрузки данных из JSON-файла
def load_data_from_json(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {file_name}.")
        return None

# Функция для сохранения результатов в JSON-файл
def save_results_to_json(user_name, correct_count, incorrect_count, knowledge_result, user_choice, directory='results'):
    
    create_directory(directory)  # Создаем папку, если она не существует
    
    results = {
        "Имя": user_name,
        "Уровень сложносности": user_choice,
        "Правильные ответы": correct_count,
        "Неправильные ответы": incorrect_count,
        "Уровень знаний": knowledge_result
    }
    
    # Создаем имя файла на основе имени пользователя и используя другую папку
    file_name = os.path.join(directory, f"{user_name}_results.json")
    
    # Сохраняем результаты в JSON-файл
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)
    
    print(f"Результаты сохранены в файл {file_name}")