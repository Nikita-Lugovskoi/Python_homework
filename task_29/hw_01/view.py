from controllers import ShoeController
from models import Shoe

def main():
    controller = ShoeController()

    while True:
        print("\n1. Добавить обувь")
        print("2. Показать всю обувь")
        print("3. Показать обувь по индексу")
        print("4. Удалить обувь по индексу")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            shoe_type = input("Введите тип обуви (мужская/женская): ")
            shoe_kind = input("Введите вид обуви: ")
            color = input("Введите цвет: ")
            price = float(input("Введите цену: "))
            manufacturer = input("Введите производителя: ")
            size = float(input("Введите размер: "))
            new_shoe = Shoe(shoe_type, shoe_kind, color, price, manufacturer, size)
            controller.add_shoe(new_shoe)

        elif choice == '2':
            shoes = controller.get_all_shoes()
            print("Вся обувь:")
            for index, shoe in enumerate(shoes):
                print(f"{index}: {shoe}")

        elif choice == '3':
            index = int(input("Введите индекс обуви: "))
            shoe = controller.get_shoe(index)
            if shoe:
                print("Обувь:", shoe)
            else:
                print("Обувь не найдена.")

        elif choice == '4':
            index = int(input("Введите индекс обуви для удаления: "))
            controller.delete_shoe(index)

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()