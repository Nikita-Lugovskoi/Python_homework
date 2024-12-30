from double_linked_list import Node
from double_linked_list import LinkedList

class ExtendedLinkedList(LinkedList):

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def insert_at_index(self, index, data):
        if index < 0:
            return "Индекс не может быть отрицательным."
        
        if index == 0:
            return self.insert_at_head(data)
        
        new_node = Node(data)
        current_node = self.head
        current_index = 0
        
        while current_node is not None and current_index < index:
            if current_index == index - 1:
                new_node.next_node = current_node
                new_node.prev_node = current_node.prev_node
                if current_node.prev_node is not None:
                    current_node.prev_node.next_node = new_node
                current_node.prev_node = new_node
                if new_node.prev_node is None:  # Если вставляем в начало
                    self.head = new_node
                return f"Вставлен узел с данными {data} на индекс {index}"
            current_node = current_node.next_node
            current_index += 1
        
        # Если индекс больше длины списка, добавляем в конец
        return self.insert_at_tail(data)

    def remove_node_index(self, index):
        if index < 0 or self.head is None:
            return "Индекс не может быть отрицательным или список пуст."
        
        current_node = self.head
        current_index = 0
        
        while current_node is not None:
            if current_index == index:
                if current_node.prev_node is not None:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node is not None:
                    current_node.next_node.prev_node = current_node.prev_node
                if current_node == self.head:  # Если удаляем голову
                    self.head = current_node.next_node
                if current_node == self.tail:  # Если удаляем хвост
                    self.tail = current_node.prev_node
                return f"Удален узел с данными {current_node.data} по индексу {index}"
            current_node = current_node.next_node
            current_index += 1
        
        return "Узел с таким индексом не найден."

    def remove_node_data(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev_node is not None:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node is not None:
                    current_node.next_node.prev_node = current_node.prev_node
                if current_node == self.head:  # Если удаляем голову
                    self.head = current_node.next_node
                if current_node == self.tail:  # Если удаляем хвост
                    self.tail = current_node.prev_node
                return f"Удален узел с данными {data}"
            current_node = current_node.next_node
        return "Узел с такими данными не найден."

    def len_ll(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next_node
        return length

    def contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, from_head=True):
        if from_head:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)

# Примеры использования
if __name__ == "__main__":
    # Создаем экземпляр расширенного двусвязного списка
    extended_list = ExtendedLinkedList()

    # Вставляем элементы
    print(extended_list.insert_at_head(10))  # Вставка 10 в голову
    print(extended_list.insert_at_tail(20))   # Вставка 20 в хвост
    print(extended_list.insert_at_tail(30))   # Вставка 30 в хвост
    print(extended_list.insert_at_index(1, 15)) # Вставка 15 на индекс 1
    print(extended_list.print_ll_from_tail())  # Печать списка с конца
    print(extended_list.len_ll())               # Получение длины списка

    # Проверка на содержание
    print(extended_list.contains_from_head(15))  # Проверка наличия 15 с головы
    print(extended_list.contains_from_tail(30))   # Проверка наличия 30 с хвоста
    print(extended_list.contains_from(20, from_head=True))  # Проверка наличия 20 с головы

    # Удаление по индексу
    print(extended_list.remove_node_index(1))  # Удаление узла по индексу 1
    print(extended_list.print_ll_from_tail())   # Печать списка с конца после удаления

    # Удаление по данным
    print(extended_list.remove_node_data(20))   # Удаление узла с данными 20
    print(extended_list.print_ll_from_tail())    # Печать списка с конца после удаления

    # Проверка длины списка после удалений
    print(extended_list.len_ll())                 # Получение длины списка после удалений
    print(extended_list.contains_from(10, from_head=False))  # Проверка наличия 10 с хвоста