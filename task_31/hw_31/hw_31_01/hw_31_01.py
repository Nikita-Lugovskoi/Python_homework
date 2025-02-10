# Создайте приложение для эмуляции работы пиццерии.
# Приложение должно иметь следующую
# функциональность:
# Пользователь может выбрать из пяти стандартных
# рецептов пиццы или создать свой рецепт.
# Пользователь может выбирать добавлять ли
# топпинги.
# Информацию о заказанной пицце нужно отображать
# на экран и сохранять в файл.
# Необходимо иметь возможность просмотреть
# количество проданных пицц, выручку, прибыль.
# добавить интерфейс для админа, в котором можно
# было бы осуществлять изменения в меню
# Классы приложения должны быть построены с
# учетом принципов SOLID и паттернов
# проектирования.

import json

class Pizza:
    def __init__(self, name, base_price, toppings=None):
        self.name = name
        self.base_price = base_price
        self.toppings = toppings if toppings else []
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def calculate_price(self):
        return self.base_price + len(self.toppings) * 1.5  # цена за топпинг

    def __str__(self):
        return f"{self.name} с топпингами: {', '.join(self.toppings)} - {self.calculate_price()}$"


class PizzaMenu:
    def __init__(self):
        self.pizzas = [
            Pizza("Маргарита", 5.0),
            Pizza("Пепперони", 6.0),
            Pizza("Гавайская", 7.0),
            Pizza("Четыре сыра", 8.0),
            Pizza("Вегетарианская", 6.5)
        ]
    
    def display_menu(self):
        for i, pizza in enumerate(self.pizzas):
            print(f"{i + 1}. {pizza}")


class Order:
    def __init__(self, pizza):
        self.pizza = pizza
        self.price = pizza.calculate_price()


class OrderManager:
    def __init__(self):
        self.orders = []
        self.total_sales = 0.0
        self.total_profit = 0.0

    def add_order(self, order):
        self.orders.append(order)
        self.total_sales += order.price
        self.total_profit += order.price - 5.0  # Предположим, что себестоимость пиццы 5$

    def save_orders(self):
        with open('hw_31/hw_31_01/orders.json', 'w') as f:
            json.dump([{'pizza': order.pizza.name, 'price': order.price} for order in self.orders], f)

    def display_stats(self):
        print(f"Количество проданных пицц: {len(self.orders)}")
        print(f"Выручка: {self.total_sales}$")
        print(f"Прибыль: {self.total_profit}$")


class AdminInterface:
    def __init__(self, menu):
        self.menu = menu

    def add_pizza(self, name, base_price):
        new_pizza = Pizza(name, base_price)
        self.menu.pizzas.append(new_pizza)
        print(f"Пицца '{name}' добавлена в меню.")


class Main:
    def __init__(self):
        self.menu = PizzaMenu()
        self.order_manager = OrderManager()
        self.admin_interface = AdminInterface(self.menu)

    def user_interface(self):
        while True:
            print("\n1. Посмотреть меню")
            print("2. Заказать пиццу")
            print("3. Посмотреть статистику")
            print("4. Выйти")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.menu.display_menu()
            elif choice == '2':
                self.menu.display_menu()
                pizza_choice = int(input("Выберите номер пиццы: ")) - 1
                toppings = input("Введите топпинги через запятую (или оставьте пустым): ").split(',')
                pizza = self.menu.pizzas[pizza_choice]
                for topping in toppings:
                    if topping.strip():
                        pizza.add_topping(topping.strip())
                order = Order(pizza)
                self.order_manager.add_order(order)
                self.order_manager.save_orders()
                print(f"Ваш заказ: {order.pizza}")
            elif choice == '3':
                self.order_manager.display_stats()
            elif choice == '4':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def admin_interface(self):
        while True:
            print("\n1. Добавить пиццу")
            print("2. Выйти")
            choice = input("Выберите действие: ")

            if choice == '1':
                name = input("Введите название пиццы: ")
                base_price = float(input("Введите базовую цену пиццы: "))
                self.admin_interface.add_pizza(name, base_price)
            elif choice == '2':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main = Main()
    while True:
        print("\n1. Пользовательский интерфейс")
        print("2. Административный интерфейс")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            main.user_interface()
        elif choice == '2':
            main.admin_interface()
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")