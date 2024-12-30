class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"


if __name__ == "__main__":
    # Создаем экземпляр двусвязного списка
    linked_list = LinkedList()

    # Вставляем элементы в список
    print(linked_list.insert_at_head(10))  # Вставка 10 в голову
    print(linked_list.insert_at_head(20))  # Вставка 20 в голову
    print(linked_list.insert_at_tail(30))   # Вставка 30 в хвост
    print(linked_list.insert_at_tail(40))   # Вставка 40 в хвост

    # Печатаем список с головы
    print("Список с головы:")
    linked_list.print_ll_from_head()

    # Удаляем элементы из списка
    print(linked_list.remove_from_head())  # Удаление из головы
    print(linked_list.remove_from_tail())  # Удаление из хвоста

    # Печатаем список после удаления
    print("Список после удаления:")
    linked_list.print_ll_from_head()
