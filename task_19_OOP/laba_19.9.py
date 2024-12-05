# Задание 1. Используя понятие множественного наследования, разработайте класс "Окружность, вписанная в квадрат"
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius
        
    def get_circle_data(self):
        perimeter = 2 * 3.14 * self.radius
        square = 3.14 * self.radius * self.radius
        return f'Радиус окружности: {self.radius}\nПериметр окружности равен: {round(perimeter, 2)}\nПлощадь окружности равна: {round(square, 2)}'
    
    
class Square:
    
    def __init__(self, side):
        self.side = side
        
    def get_side(self):
        return self.side
    
    def set_side(self, side):
        self.side = side
            
    def get_square_data(self):
        perimeter = 4 * self.side
        square = self.side * self.side
        return f'Сторона квадрата равна: {self.side}\nПериметр квадрата равен: {perimeter}\nПлощадь квадрата равна: {square}'
    

class Circle_in_Spuare(Circle, Square):
    
    def __init__(self, radius, side):
        super().__init__(radius)
        Square.__init__(self, side)
        
    def show_if_it_can_be(self):
        if self.radius == self.side / 2:
            print(f'Поздравляю! В квадрат со стороной {self.side} можно вписать окружность радиусом {self.radius}.')
        else:
            print(f'Увы. В квадрат со стороной {self.side} нельзя вписать окружность радиусом {self.radius}.')

print("Учтите, для того чтобы вписать окружность в квадрат, ее радиус должен быть равен стороне квадрата деленной пополам!")

radius = int(input("Введите радиус окружности: "))
side = int(input("Введите сторону квадрата: "))
print()

data = Circle_in_Spuare(radius, side)

print(data.get_circle_data())
print()
print(data.get_square_data())
print()
print(data.show_if_it_can_be())


# Задание 2. Используя механизм множественного наследования разработайте класс “Автомобиль”. Должны быть классы «Колеса», «Двигатель», «Двери» и т.д.
class Wheel:
    
    def rotate(self):
        print("Колесо вращается")
        
    def not_rotate(self):
        print("Колесо больше не вращается")

class Engine:
    
    def start(self):
        print("Двигатель запущен")
        
    def stop(self):
        print("Двигатель остановлен")
        
class Door:
   
    def open(self):
        print("Дверь открыта")
    
    def close(self):
        print("Дверь закрыта")
        
class Car:
    def __init__(self):
        self.engine = Engine() 
        self.wheels = [Wheel() for i in range(4)]
        self.door = Door()  
        
    def start(self):
        self.door.open()
        self.door.close()
        self.engine.start()  
        for wheel in self.wheels:
            wheel.rotate()  
        for wheel in self.wheels:
            wheel.not_rotate()
        self.engine.stop()
        self.door.open()
        self.door.close()
        
            
# Создаем автомобиль и запускаем его
my_car = Car()
my_car.start()


# Задание 3
# Создать базовый класс «Домашнее животное» и производные классы «Собака», «Кошка», «Попугай», «Хомяк».
# С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого из классов методы:
# ■ Sound — издает звук животного (пишем текстом в
# консоль);
# ■ Show — отображает имя животного;
# ■ Type — отображает название его подвида;

class Pet:
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def Show(self):
        print(f'Имя животного: {self.name}')
        
    
class Dog(Pet):
    
    def Sound(self):
        print("Гав-Гав!")
        
    def Age(self):
        print(f"Возраст: {self.age} год")
        
    def Type(self):
        return "Собака"
    
class Cat(Pet):
    
    def Sound(self):
        print("Мяу-мяу!")
        
    def Age(self):
        print(f"Возраст: {self.age} год")

    def Type(self):
        return "Кошка"
    
    
class Parrot(Pet):
    
    def Sound(self):
        print("Кар-кар!")
        
    def Age(self):
        print(f"Возраст: {self.age} год")

    def Type(self):
        return "Попугай"
    
    
class Hamster(Pet):
    
    def Sound(self):
        print("Пи-пи!")
        
    def Age(self):
        print(f"Возраст: {self.age} год")

    def Type(self):
        return "Хомяк"
    

dog = Dog("Шарик", 1)
dog.Show()
dog.Sound()
dog.Age()
print(f"Тип: {dog.Type()}")
print()

cat = Cat("Мурка", 2)
cat.Show()
cat.Sound()
cat.Age()
print(f"Тип: {cat.Type()}")
print()

parrot = Parrot("Кеша", 3)
parrot.Show()
parrot.Sound()
parrot.Age()
print(f"Тип: {parrot.Type()}")
print()

hamster = Hamster("Хомка", 4)
hamster.Show()
hamster.Sound()
hamster.Age()
print(f"Тип: {hamster.Type()}")




# Задание 4
# Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию о служащем. 
# В случае базового класса это может быть строка с ндписья this is Employer class 
# Создайте от него три производных класса: President, Manager, Worker. 
# Переопределите функцию Prin для вывода информации, соответствующей каждому типу служащего.

class Employer:
    def Print(self):
        print("This is Employer class")

class President(Employer):
    def Print(self):
        print("This is President class")

class Manager(Employer):
    def Print(self):
        print("This is Manager class")

class Worker(Employer):
    def Print(self):
        print("This is Worker class")

# Пример использования
if __name__ == "__main__":
    employer = Employer()
    employer.Print()  

    president = President()
    president.Print()  

    manager = Manager()
    manager.Print()  

    worker = Worker()
    worker.Print()  
    
    
# Задание 5
# Для классов из задания 4 реализуйте магический метод str, а также метод int (должен возвращать возраст служащего).

class Employer:
    def __init__(self, age):
        self.age = age

    def Print(self):
        print("This is Employer class")

    def __str__(self):
        return "Employer"

    def __int__(self):
        return self.age

class President(Employer):
    def __init__(self, age):
        super().__init__(age)

    def Print(self):
        print("This is President class")

    def __str__(self):
        return "President"

class Manager(Employer):
    def __init__(self, age):
        super().__init__(age)

    def Print(self):
        print("This is Manager class")

    def __str__(self):
        return "Manager"

class Worker(Employer):
    def __init__(self, age):
        super().__init__(age)

    def Print(self):
        print("This is Worker class")

    def __str__(self):
        return "Worker"

if __name__ == "__main__":
    employer = Employer(45)
    employer.Print()  
    print(str(employer))  
    print(int(employer)) 

    president = President(50)
    president.Print()  
    print(str(president))  
    print(int(president))  

    manager = Manager(35)
    manager.Print()  
    print(str(manager))  
    print(int(manager))  

    worker = Worker(28)
    worker.Print()  
    print(str(worker))  
    print(int(worker))  