class Node:
    """Класс, представляющий узел в связном списке."""
    """Инициализация узла."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс, представляющий стек на основе связного списка."""
    """Инициализация стека."""
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    """Добавляет элемент на вершину стека."""
    def push(self, data):
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    """ Удаляет и возвращает верхний элемент стека."""
    def pop(self):
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    """ Проверяет, пуст ли стек."""
    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    """ Проверяет, полон ли стек."""
    def is_full(self):
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    """Очищает стек, удаляя все элементы."""
    def clear_stack(self):
        while self.top:
            self.pop()

    """Получает данные по индексу."""
    def get_data(self, index):
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    """Возвращает текущее количество элементов в стеке."""
    def size_stack(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    """Считает количество целых чисел в стеке."""
    def counter_int(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


stack = Stack()
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
print(stack.counter_int())
