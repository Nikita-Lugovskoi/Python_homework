# Задание 8.1.1
class Vehicle:
    
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
        
    def get_vehicle_type(self, num_of_wheels):
        if num_of_wheels == 2:
            return f'Это мотоцикл марки {self.name}.'
        elif num_of_wheels == 3:
            return f'Это трицикл марки {self.name}.'
        elif num_of_wheels == 4:
            return f'Это автомобиль марки {self.name}.'
        else:
            return f'Я не знаю таких ТС.'
        
    def get_vehicle_advice(self):
        if self.mileage <= 50000:
            return f'Неплохо {self.name} можно брать.'
        elif 50001 <= self.mileage <= 100000:
            return f'{self.name} надо внимательно проверить.'
        elif 100001 <= self.mileage <= 150000:
            return f'{self.name} надо провести полную диагностику.'
        elif self.mileage > 150000:
            return f'{self.name} лучше не покупать.'
        
my_first_car = Vehicle("БМВ", 30000)
my_second_car = Vehicle("AUDI", 51001)
my_fird_car = Vehicle("Митсубиши", 120000)
my_fourth_car = Vehicle("Mercedes", 160000)

print(my_first_car.get_vehicle_type(1))
print(my_first_car.get_vehicle_advice())
print()
print(my_second_car.get_vehicle_type(2))
print(my_second_car.get_vehicle_advice())
print()
print(my_fird_car.get_vehicle_type(3))
print(my_fird_car.get_vehicle_advice())
print()
print(my_fourth_car.get_vehicle_type(4))
print(my_fourth_car.get_vehicle_advice())


# Задание 8.1.2
class Students:
    def __init__(self, name, surname, age, city, phone, email, languages):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.phone = phone
        self.email = email
        self.languages = languages
    
    def get_data(self):
        return f'Студент: {self.name.capitalize()} {self.surname.capitalize()}, возраст: {self.age}, живет в городе: {self.city.capitalize()}, телефон: {self.phone}, email: {self.email}, владеет языками программирования: {self.languages}.'
    
    def set_phone(self, new_phone):
        self.phone = new_phone
        
    def set_email(self, new_email):
        self.email = new_email
    
    def set_languages(self, new_languages):
        self.languages = new_languages
        
student_name = input("Введите Ваше имя: ").strip()
student_surname = input("Введите Вашу фамилию: ").strip()
student_age = int(input("Введите Ваш возраст: "))
student_city = input("Введите Ваш город: ").strip()
student_phone = input("Введите Ваш телефон: ").strip()
student_email = input("Введите Ваш email: ").strip()
student_languages = input("Введите языки программирования, которыми вы владеете: ")

first_student = Students(student_name, student_surname, student_age, student_city, student_phone, student_email, student_languages)
print(first_student.get_data())  

new_phone = input("Введите новый телефон: ").strip()
new_email = input("Введите новый email: ").strip()
new_languages = input("Введите языки, которые вы забыли указать: ")

first_student.set_phone(new_phone)
first_student.set_email(new_email)
first_student.set_languages(new_languages)

print(first_student.get_data())  


# Вопрос: как сделать так, чтобы new_languages добавилась к предыдущему languages, а не заменила его?