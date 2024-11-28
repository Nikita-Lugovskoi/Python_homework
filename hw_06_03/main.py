import json
from utils import create_directory, load_data_from_json, save_results_to_json
from functions import get_user_level, base_program, get_result

def main():
    # Загрузка данных из JSON-файла 
    data = load_data_from_json("questions.json") 

    if data:
        my_list_of_questions_and_lvls = data 
        answers = {}
        words = {}

        # Запрашиваем имя пользователя
        user_name = input("Введите ваше имя: ").strip()

        # Просим ввести уровень сложности и определяем, к какому из словарей будем обращаться
        user_choice = input("Введите уровень сложности: easy, medium или hard ").strip().lower()        

        # Вызываем функцию для опредения нужного нам словаря по выбору пользователя
        user_lvl = get_user_level(user_choice, my_list_of_questions_and_lvls)     
        
        # Вызываем функцию для перебора элементов словаря и сравнения их с ответами пользователя
        result_answers = base_program(user_lvl)
        
        # Обращаемся к словарю levels и записываем в переменную
        english_lvls = my_list_of_questions_and_lvls[1]['levels']

        # Вызываем функцию для подсчета и вывода ответов, также определния уровня знаний пользователя
        knowledge_result = get_result(result_answers, english_lvls)
        print(f'Ваш уровень знаний: {knowledge_result}')

        # Сохраняем результаты в JSON-файл
        correct_count = len([key for key in result_answers if result_answers[key] == "True"])
        incorrect_count = len([key for key in result_answers if result_answers[key] == "False"])
        save_results_to_json(user_name, correct_count, incorrect_count, knowledge_result, user_choice, directory='results')

if __name__ == "__main__":
    main()