# При старте приложения запускаются три потока.
# Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список
# заполнен оба потока запускаются. Первый поток
# находит сумму элементов списка, второй поток
# среднеарифметическое значение в списке. Полученный
# список, сумма и среднеарифметическое выводятся на
# экран.

import threading
import random
import time

numbers = []
list_filled = threading.Event()

# Функция для заполнения списка случайными числами
def fill_list(size):
    global numbers
    for i in range(size):
        numbers.append(random.randint(1, 100))
    list_filled.set()  # Устанавливаем событие, чтобы уведомить другие потоки

# Функция для вычисления суммы элементов списка
def calculate_sum():
    list_filled.wait()  # Ожидаем, пока список не будет заполнен
    total_sum = sum(numbers)
    print(f"Сумма элементов списка: {total_sum}")

# Функция для вычисления среднеарифметического значения
def calculate_average():
    list_filled.wait()  # Ожидаем, пока список не будет заполнен
    if numbers:  
        average = sum(numbers) / len(numbers)
        print(f"Среднеарифметическое значение: {average}")
    else:
        print("Список пуст, среднеарифметическое значение не может быть вычислено.")

# Основная часть программы
if __name__ == "__main__":
    size = 10  
    fill_thread = threading.Thread(target=fill_list, args=(size,))
    sum_thread = threading.Thread(target=calculate_sum)
    average_thread = threading.Thread(target=calculate_average)

    # Запускаем потоки
    fill_thread.start()
    sum_thread.start()
    average_thread.start()

    # Ждем завершения потоков
    fill_thread.join()
    sum_thread.join()
    average_thread.join()

    # Выводим заполненный список
    print(f"Заполненный список: {numbers}")