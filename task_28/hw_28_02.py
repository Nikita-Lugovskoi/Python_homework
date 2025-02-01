# Создайте приложение для работы в библиотеке. 
# Оно должно оперировать следующими сущностями: Книга, Библиотекарь, Читатель. 
# Приложение должно позволять вводить, удалять, изменять, сохранять вфайл, загружать из файла, логгировать действия, искать информацию (результаты поиска выводятся на экран или файл) о сущностях. 
# При реализации используйте максимально возможное количество паттернов проектирования. 
# Также необходимо пояснить почему было решено использовать именно данные паттерны.

import json
import logging

# Настройка логгирования
logging.basicConfig(filename='library.log', level=logging.INFO)

# Сущности
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Librarian:
    def __init__(self, name):
        self.name = name

class Reader:
    def __init__(self, name):
        self.name = name

# Фабрика
class EntityFactory:
    @staticmethod
    def create_book(title, author):
        return Book(title, author)

# Библиотека
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        logging.info(f'Added book: {book.title}')

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        logging.info(f'Removed book: {title}')

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            books_data = json.load(f)
            self.books = [Book(**data) for data in books_data]

    def search(self, query):
        return [book for book in self.books if query.lower() in book.title.lower()]

# Пример использования
library = Library()

# Добавление книг
book1 = EntityFactory.create_book("1984", "George Orwell")
book2 = EntityFactory.create_book("Brave New World", "Aldous Huxley")
library.add_book(book1)
library.add_book(book2)

# Сохранение библиотеки в файл
library.save_to_file('library.json')

# Загрузка библиотеки из файла
library.load_from_file('library.json')

# Поиск книг по названию
found_books = library.search("1984")
for book in found_books:
    print(f'Found book: {book.title} by {book.author}')