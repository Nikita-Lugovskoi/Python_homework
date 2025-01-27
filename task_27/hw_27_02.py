# Создайте приложение для приготовления пасты.
# Приложение должно уметь создавать минимум три вида пасты. 
# Классы различной пасты должны иметь следующие методы:
# Тип пасты; Соус; Начинка; Добавки.
# Для реализации используйте порождающие паттерны, те которые посчитаете наиболее подходящими, также
# напишите почему именно эти паттерны вы решили использовать.

from abc import ABC, abstractmethod

# Базовый класс для пасты
class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additions(self):
        pass

# Конкретные классы пасты
class Spaghetti(Pasta):
    def get_type(self):
        return "Спагетти"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Мясной фарш"

    def get_additions(self):
        return "Пармезан, базилик"

class Penne(Pasta):
    def get_type(self):
        return "Пенне"

    def get_sauce(self):
        return "Сливочный соус"

    def get_filling(self):
        return "Курица"

    def get_additions(self):
        return "Грибы, шпинат"

class Fettuccine(Pasta):
    def get_type(self):
        return "Феттучини"

    def get_sauce(self):
        return "Алфредо"

    def get_filling(self):
        return "Креветки"

    def get_additions(self):
        return "Чеснок, лимон"

# Фабрика для создания пасты
class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "spaghetti":
            return Spaghetti()
        elif pasta_type == "penne":
            return Penne()
        elif pasta_type == "fettuccine":
            return Fettuccine()
        else:
            raise ValueError("Unknown pasta type")

# Пример использования
if __name__ == "__main__":
    pasta_type = input("Введите тип пасты (spaghetti, penne, fettuccine): ")
    pasta = PastaFactory.create_pasta(pasta_type)

    print(f"Тип пасты: {pasta.get_type()}")
    print(f"Соус: {pasta.get_sauce()}")
    print(f"Начинка: {pasta.get_filling()}")
    print(f"Добавки: {pasta.get_additions()}")
    
    
"""Паттерн Фабрика
Паттерн Фабрика позволяет создавать объекты без указания конкретного класса создаваемого объекта. Это удобно, когда у нас есть несколько видов пасты, и мы хотим скрыть детали их создания.

    Паттерн Строитель
Паттерн Строитель позволяет создавать сложные объекты поэтапно. В нашем случае это может быть полезно для создания пасты с различными параметрами, такими как соус, начинка и добавки."""