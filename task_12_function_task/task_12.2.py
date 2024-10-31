# Задание 4/1 - 1
# def my_text():
#     print(
# """“Don't compare yourself with anyone in this world…
# if you do so, are insulting yourself.”
#                                                Bill Gates""")
    
# my_text()


# Задание 4/1 - 2
# def even_nums(x, y):
#     for i in range(x, y):
#         if i % 2 == 0:
#             print(i)

# even_nums(1, 7)


# Задание 4/1 - 3
# def draw_square(side_length, symbol, filled):
#     if filled:
#         for i in range(side_length):
#             print(symbol * side_length)
#     else:
#         for i in range(side_length):
#             if i == 0 or i == side_length - 1:
#                 print(symbol * side_length)  # верхняя и нижняя грани
#             else:
#                 print(symbol + ' ' * (side_length - 2) + symbol)  # пустые строки между гранями

# print("Заполненный квадрат:")
# draw_square(5, '*', True)

# print("\nПустой квадрат:")
# draw_square(5, '*', False)


# Задание 4/1 - 4
# def min_num(num_list):
#     print(min(num_list))
    
# my_list = [1, 12, 3, 5, -1]
# min_num(my_list)


# Задание 4/1 - 5
# def my_multiplication(start, stop):
#     multiplication = 1
    
#     if start > stop:
#         start, stop = stop, start
        
#     for i in range(start, stop + 1):
#         multiplication *= i
        
#     return multiplication

# result = my_multiplication(5, 3)
# print(result)


# Задание 4/1 - 6
# def count_digits(number):

#     return len(str(abs(number)))

# print(count_digits(3456))  
# print(count_digits(-67539)) 
# print(count_digits(0))      
            

# Задание 4/1 - 7
# def is_palindrome(num):
#     num = str(num)
#     if num[::] == num[::-1]:
#         return True
#     else:
#         return False
    
# result_1 = is_palindrome(123321)
# result_2 = is_palindrome(546645)
# result_3 = is_palindrome(421987)
# print(result_1)
# print(result_2)
# print(result_3)
