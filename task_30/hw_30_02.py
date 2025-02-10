# Пользователь с клавиатуры вводит путь к файлу. После
# чего запускаются три потока. Первый поток заполняет
# файл случайными числами. Два других потока ожидают
# заполнения. Когда файл заполнен оба потока стартуют.
# Первый поток находит все простые числа, второй поток
# факториал каждого числа в файле. Результаты поиска
# каждый поток должен записать в новый файл. На экран
# необходимо отобразить статистику выполненных
# операций.


import threading
import random
import math
import os

file_path = ""
list_filled = threading.Event()

# Функция для заполнения файла случайными числами
def fill_file(file_path, size):
    with open(file_path, 'w') as f:
        for _ in range(size):
            f.write(f"{random.randint(1, 100)}\n")
    list_filled.set()  # Устанавливаем событие, чтобы уведомить другие потоки

# Функция для нахождения простых чисел
def find_primes(output_file):
    list_filled.wait()  # Ожидаем, пока файл не будет заполнен
    primes = []
    with open(file_path, 'r') as f:
        for line in f:
            num = int(line.strip())
            if is_prime(num):
                primes.append(num)
    
    with open(output_file, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")
    
    print(f"Найдено простых чисел: {len(primes)}")

# Функция для вычисления факториалов
def calculate_factorials(output_file):
    list_filled.wait()  # Ожидаем, пока файл не будет заполнен
    factorials = []
    with open(file_path, 'r') as f:
        for line in f:
            num = int(line.strip())
            factorials.append((num, math.factorial(num)))
    
    with open(output_file, 'w') as f:
        for num, fact in factorials:
            f.write(f"{num}! = {fact}\n")
    
    print(f"Вычислено факториалов: {len(factorials)}")

# Функция для проверки, является ли число простым
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Основная часть программы
if __name__ == "__main__":
    file_path = input("Введите путь к файлу для заполнения: ")
    size = 10  # Количество случайных чисел
    primes_output_file = "primes.txt"
    factorials_output_file = "factorials.txt"

    # Создаем потоки
    fill_thread = threading.Thread(target=fill_file, args=(file_path, size))
    primes_thread = threading.Thread(target=find_primes, args=(primes_output_file,))
    factorials_thread = threading.Thread(target=calculate_factorials, args=(factorials_output_file,))

    # Запускаем потоки
    fill_thread.start()
    primes_thread.start()
    factorials_thread.start()

    # Ждем завершения потоков
    fill_thread.join()
    primes_thread.join()
    factorials_thread.join()

    # Выводим статистику
    print(f"Файл '{file_path}' заполнен случайными числами.")
    print(f"Результаты простых чисел записаны в '{primes_output_file}'.")
    print(f"Результаты факториалов записаны в '{factorials_output_file}'.")