"""Реализовать класс «Книга» у которого будет минимум 3
атрибута и 2 метода добавьте возможность упаковки и
распаковки данных с использованием json и pickle, для
json метод упаковки через Encoder."""

import json
import pickle

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def pack_json(self):
        """Упаковка данных в JSON формат с использованием Encoder."""
        return json.dumps(self, cls=BookEncoder)

    @classmethod
    def unpack_json(cls, json_data):
        """Распаковка данных из JSON формата."""
        data = json.loads(json_data)
        return cls(data['title'], data['author'], data['year'])

    def pack_pickle(self):
        """Упаковка данных в Pickle формат."""
        return pickle.dumps(self)

    @classmethod
    def unpack_pickle(cls, pickle_data):
        """Распаковка данных из Pickle формата."""
        return pickle.loads(pickle_data)

class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                'title': obj.title,
                'author': obj.author,
                'year': obj.year
            }
        return super().default(obj)

# Пример использования
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)

    # Упаковка в JSON
    json_data = book.pack_json()
    print("Упакованные данные в JSON:", json_data)

    # Распаковка из JSON
    unpacked_book = Book.unpack_json(json_data)
    print("Распакованная книга:", unpacked_book.title, unpacked_book.author, unpacked_book.year)

    # Упаковка в Pickle
    pickle_data = book.pack_pickle()
    print("Упакованные данные в Pickle:", pickle_data)

    # Распаковка из Pickle
    unpacked_book_pickle = Book.unpack_pickle(pickle_data)
    print("Распакованная книга из Pickle:", unpacked_book_pickle.title, unpacked_book_pickle.author, unpacked_book_pickle.year)