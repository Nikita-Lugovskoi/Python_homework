# # Задача 5.1.1
# styles_tuple = ("Роман", "Новелла", "Фентези", "Научная Фантастика")
# nums_tuple = (3, 7, 9, 1, 6, 8, 2, 5, 4)

# # узнайте длину обоих кортежей (это количество элементов в них);
# print(len(styles_tuple))
# print(len(nums_tuple))

# # найдите максимальный и минимальный элемент
# print(max(styles_tuple))
# print(min(styles_tuple))
# print(max(nums_tuple))
# print(min(nums_tuple))

# # просуммируйте элементы если это возможно
# print(sum(nums_tuple))

# # отсортируйте элементы по возрастанию и убыванию в
# # результате сортировки и последующих операций необходимо
# # получить кортеж.
# sorted_ascending_styles_tuple = tuple(sorted(styles_tuple))
# sorted_ascending_nums_tuple = tuple(sorted(nums_tuple))
# sorted_descending_styles_tuple = tuple(sorted(styles_tuple, reverse=True))
# sorted_descending_nums_tuple = tuple(sorted(nums_tuple, reverse=True))

# print("Кортеж жанров, отсортированный по возрастанию:", sorted_ascending_styles_tuple)
# print("Кортеж чисел, отсортированный по возрастанию:", sorted_ascending_nums_tuple)
# print("Кортеж жанров, отсортированный по убыванию:", sorted_descending_styles_tuple)
# print("Кортеж чисел, отсортированный по убыванию:", sorted_descending_nums_tuple)


# # Задача 5.1.2
# cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")

# # заменить жанр Экшн на Боевик
# cinema_genres_list = list(cinema_genres)

# for i in range(len(cinema_genres_list)):
#     if cinema_genres_list[i] == "Экшн":
#         cinema_genres_list[i] = "Боевик"

# new_cinema_genres = tuple(cinema_genres_list)
# print(new_cinema_genres)

# # добавить жанр по вашему выбору между жанрами боевик и пеплум
# new_cinema_genres = list(cinema_genres)

# cinema_genres_list.insert(2, "Детектив")
# update_cinema_genres_list = tuple(cinema_genres_list)
# print(update_cinema_genres_list)

# # преобразовать полученный кортеж в строку. Результат вывести в консоль
# string_cinema_elements = map(str, update_cinema_genres_list)
# result_string = ', '.join(string_cinema_elements)
# print("Результат преобразования кортежа в строку:", result_string)

# # Задача 5.1.3
my_tools = {"вода", "топор", "еда", "нитки", "одежда", "компас", "карта", "спички", "изолента", "доски"}
my_fathers_tools = {"гвозди", "антисептик", "котелок", "ложка", "вилка", "компас", "спички", "вода", "топор", "еда"}

# вещи, которые взяли вы бы двое
union_tools = my_tools | my_fathers_tools 
print(union_tools)

# вещи, которые возьмцу только я
print(my_tools)

# вещи, которые возьмет отец
print(my_fathers_tools)

# вещи, которые есть и у меня и у него
intersection_tools = my_tools & my_fathers_tools 
print(intersection_tools)

# # Задача 5.1.4
# cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

# # преобразовать список в множество
# cinema_genres_set = set(cinema_genres)
# print(cinema_genres_set)

# # добавить 2 жанра
# cinema_genres_set.add("детектив")
# cinema_genres_set.add("хоррор")
# print(cinema_genres_set)

# # удалить любой из жанров
# cinema_genres_set.remove("экшн")
# print(cinema_genres_set)

# # удалить случайный жарн
# cinema_genres_set.pop()
# print(cinema_genres_set)

# # преобразовать множество в список
# new_cinema_genres = list(cinema_genres_set)
# print(new_cinema_genres)