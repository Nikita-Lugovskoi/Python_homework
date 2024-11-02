import re

# Паттерны для проверки данных
def get_reg_data():
    
    return [
        r'^\w+(@yandex\.ru)+$',  # Email
        r'^[+]\d{1,3}\(\d{2}\)(\d{7})$',  # Телефон
        r'^[a-zA-Zа-яА-Я]+$',  # Имя 
        r'^[a-zA-Zа-яА-Я]+$'  # Фамилия 
    ]
      
# Проверка уникальности данных  
def check_unique_data(user_data, data_to_check):

    return user_data not in data_to_check

# Проверка введенных данных
def reg_check(user_data, reg_pattern, users_list, data_to_check=None):

    if re.match(reg_pattern, user_data):
        if data_to_check is not None and not check_unique_data(user_data, data_to_check):
            print("Ошибка: Данные не уникальны.")
            return None
        return user_data
    else:
        print("Ошибка: Неверный формат данных.")
        return None