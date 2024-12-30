import unittest
import sys
import os

# Добавляем родительскую папку в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LinkedListClass import LinkedList
from LinkedListClass import Queue

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_at_head(self):
        self.assertEqual(self.ll.insert_at_head(10), "Узел с данными 10 добавлен в начало списка")
        self.assertEqual(self.ll.insert_at_head(20), "Узел с данными 20 добавлен в начало списка")

    def test_remove_node_position(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_head(20)
        self.assertEqual(self.ll.remove_node_position(1), "Удален узел с данными 20 позиции 1")
        self.assertEqual(self.ll.remove_node_position(1), "Удален узел с данными 10 позиции 1")

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(3)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('A')
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        self.queue.enqueue('A')
        self.queue.enqueue('B')
        self.queue.enqueue('C')
        self.assertTrue(self.queue.is_full())

if __name__ == '__main__':
    unittest.main()