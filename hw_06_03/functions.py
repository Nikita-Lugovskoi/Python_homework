# Функция для получения словаря, соответствующего уровню сложности, который ввел пользователь.
def get_user_level(user_choice, my_list_of_questions_and_lvls):
        if user_choice == "easy":
            words = my_list_of_questions_and_lvls[0]['questions'][0]
            print("Вы выбрали легкий уровень! Удачи! \n")
            return words
        elif user_choice == "medium":
            words = my_list_of_questions_and_lvls[0]['questions'][1]
            print("Вы выбрали средний уровень! Удачи! \n")
            return words
        elif user_choice == "hard":
            words = my_list_of_questions_and_lvls[0]['questions'][2]
            print("Вы выбрали сложный уровень! Удачи! \n")
            return words
        else:
            print("Вы ввели некорректные данные. Уровень по умолчанию становится - легкий. \n")
            words = my_list_of_questions_and_lvls[0]['questions'][0]
            return words

# Функция для перебора элементов словаря и сравнения их с ответами пользователя 
def base_program(user_lvl):
        answers = {}
        for key, value in user_lvl.items():
            print(f'{key}, {len(value)} букв, начинается на {value[0]}...')
            user_answer = input("Введите ваш ответ: ").strip().lower()
            if user_answer == value:
                print(f'Верно. {key.capitalize()} - это {value}. \n') 
                answers[key] = "True"
            else:
                print(f'Неверно. {key.capitalize()} - это {value}. \n')
                answers[key] = "False"
        return answers

# Функция для подсчета и вывода ответов, также определния уровня знаний пользователя.
def get_result(result_answers, english_lvls):
        correct_answers = []
        incorrect_answers = []
        
        # Разделяем в два списка правильные и неправильные слова
        for key in result_answers:
            if result_answers[key] == "True":
                correct_answers.append(key)
            else:
                incorrect_answers.append(key)
        
        # Выводим правильные и неправильные ответы
        if correct_answers:
            print(f' Правильно отвеченные слова:')
            for answer in correct_answers:
                print(answer)
        else:
            print("Правильно отвечены слова: НЕТ \n")

        print()
        
        if incorrect_answers:
            print(f'Неправильно отвеченные слова: ')
            for answer in incorrect_answers:
                print(answer)
        else:
            print("Неправильно отвечены слова: НЕТ \n")
            
        print()
        
        # Определяем уровень знаний
        for key, value in english_lvls.items():
            if len(correct_answers) == int(key):  
                return value  
        
        return "Неопределен"