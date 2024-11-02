
from utils import get_reg_data, reg_check

def main():
    users_list = []
    
    while len(users_list) < 3:
        user_data = []
        patterns = get_reg_data()
        
        for i in range(4):  # Для каждого пользователя запрашиваем 4 данных
            if i == 0:
                prompt = "Введите email на яндексе: "
                data = input(prompt)
                checked_data = reg_check(data, patterns[i], users_list, [user[0] for user in users_list])
            elif i == 1:
                prompt = "Введите номер телефона в формате +***(**)*******: "
                data = input(prompt)
                checked_data = reg_check(data, patterns[i], users_list, [user[1] for user in users_list])
            elif i == 2:
                prompt = "Введите имя: "
                data = input(prompt)
                checked_data = reg_check(data, patterns[i], users_list)
            elif i == 3:
                prompt = "Введите фамилию: "
                data = input(prompt)
                checked_data = reg_check(data, patterns[i], users_list)

            if checked_data is not None:
                user_data.append(checked_data)
            else:
                print("Попробуйте снова.")
                break  # Выход из цикла, если данные не прошли проверку
        
        if len(user_data) == 4:  # Если все данные прошли проверку
            users_list.append(user_data)
            print("Пользователь добавлен:", user_data)

    print("Список пользователей:", users_list)

if __name__ == "__main__":
    main()