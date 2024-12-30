class Node:
    """Класс для представления узла связного списка."""
    
    def __init__(self, data, next_node=None):
        """
        Инициализация узла.
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для представления связного списка."""

    def __init__(self):
        """Инициализация пустого связного списка."""
        self.head = None

    def insert_at_head(self, data):
        """Вставка узла с данными в начало списка."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):
        """Вставка узла с данными в конец списка."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):
        """Удаление узла по заданной позиции."""
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):
        """Вставка узла с данными на заданную позицию."""
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):
        """Вывод всех данных списка."""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):
        """Поиск узла по данным."""
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):
        """Изменение данных узла."""
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"
    
    
class Queue:
    """Класс для представления очереди с фиксированным размером."""

    def __init__(self, size):
        """
        Инициализация очереди.
        """
        self.size = size
        self.queue = []
    
    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return len(self.queue) == 0

    def is_full(self):
        """Проверка, заполнена ли очередь."""
        return len(self.queue) == self.size

    def enqueue(self, item):
        """Добавление элемента в очередь."""
        if self.is_full():
            return "Очередь заполнена"
        self.queue.append(item)
        return f"Элемент {item} добавлен в очередь"

    def dequeue(self):
        """Удаление элемента из очереди."""
        if self.is_empty():
            return "Очередь пуста"
        return f"Элемент {self.queue.pop(0)} удален из очереди"

    def show(self):
        """Отображение всех элементов очереди."""
        return " -> ".join(self.queue) if self.queue else "Очередь пуста"
    

def main_menu():
    queue_size = int(input("Введите размер очереди: "))
    queue = Queue(queue_size)

    while True:
        print("\nМеню:")
        print("1. Добавить элемент в очередь")
        print("2. Удалить элемент из очереди")
        print("3. Показать элементы очереди")
        print("4. Проверить, пуста ли очередь")
        print("5. Проверить, заполнена ли очередь")
        print("6. Выход")

        choice = input("Выберите операцию: ")

        if choice == '1':
            item = input("Введите элемент для добавления: ")
            print(queue.enqueue(item))
        elif choice == '2':
            print(queue.dequeue())
        elif choice == '3':
            print(queue.show())
        elif choice == '4':
            print("Очередь пуста" if queue.is_empty() else "Очередь не пуста")
        elif choice == '5':
            print("Очередь заполнена" if queue.is_full() else "Очередь не заполнена")
        elif choice == '6':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main_menu()