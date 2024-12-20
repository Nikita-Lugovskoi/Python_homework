import unittest
from Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        """Создает новый стек перед каждым тестом."""
        self.stack = Stack()

    def test_push_and_pop(self):
        """Тестирует добавление и удаление элементов из стека."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_is_empty(self):
        """Тестирует метод is_empty."""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        """Тестирует метод is_full."""
        self.assertFalse(self.stack.is_full())

    def test_clear_stack(self):
        """Тестирует метод clear_stack."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear_stack()
        self.assertTrue(self.stack.is_empty())

    def test_get_data(self):
        """Тестирует метод get_data."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.get_data(0), 3)  # Top element
        self.assertEqual(self.stack.get_data(1), 2)  # Second element
        self.assertEqual(self.stack.get_data(2), 1)  # Bottom element
        self.assertEqual(self.stack.get_data(3), "Out of range")  # Out of range

    def test_size_stack(self):
        """Тестирует метод size_stack."""
        self.assertEqual(self.stack.size_stack(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size_stack(), 2)

    def test_counter_int(self):
        """Тестирует метод counter_int."""
        self.stack.push(1)
        self.stack.push("string")
        self.stack.push(2)
        self.stack.push(2.5)
        self.stack.push("another string")
        self.assertEqual(self.stack.counter_int(), 2)  # Only integers

if __name__ == '__main__':
    unittest.main()