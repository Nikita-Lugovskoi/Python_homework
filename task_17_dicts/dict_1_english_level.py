words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_meduim = {
    "believe": "верить",
    "feel": "чувтсвовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {
    
}

correct_answers = []
incorrect_answers = []

# просим ввести уровень сложности и определяем к какому из словарей будем обращаться
user_choice = input("Введите уровень сложности: easy, medium или hard ").strip().lower()
if user_choice == "easy":
    words = words_easy
    print("Вы выбрали легкий уровень! Удачи! \n")
elif user_choice == "medium":
    words = words_meduim
    print("Вы выбрали средний уровень! Удачи! \n")
elif user_choice == "hard":
    words = words_hard
    print("Вы выбрали сложный уровень! Удачи! \n")
else:
    print("Вы ввели некорректныве данные. Уровень по умолчанию становится - легкий. \n")
    words = words_easy
    
    
# перебираем элементы словаря и сравниваем с ответами пользователя
for key, value in words.items():
    print(f'{key}, {len(value)} букв, начинается на {value[0]}...')
    user_answer = input("Введите ваш ответ: ").lower()
    if user_answer == value:
        print(f'Верно. {key.capitalize()} - это {value}. \n')
        answers[key] = "True"
        correct_answers.append(key)
    else:
        print(f'Неверно. {key.capitalize()} - это {value}. \n')
        answers[key] = "False"
        incorrect_answers.append(key)


# выводим правильные и неправильные ответы
if correct_answers:
    print(f'Правильно отвеченные слова:')
    for answer in correct_answers:
        print(answer)
else:
    print("Правильно отвечены слова: НЕТ \n")

print()
    
if incorrect_answers:
    print(f'Неравильно отвеченные слова: ')
    for answer in incorrect_answers:
        print(answer)
else:
    print("Правильно отвечены слова: НЕТ \n")
    
print()
    

# считаем количество правильно отгаданных слов и выводим ранг
for key, value in levels.items():
    if len(correct_answers) == key:
        print(f'Ваш ранг: \n{value}')