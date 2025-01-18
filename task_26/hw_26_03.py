"""Реализовать класс «Стадион» у которого будет минимум
3 атрибута и 2 метода добавьте
возможность упаковки и распаковки данных с
использованием json и pickle, для json метод упаковки
через Adapter."""

import json
import pickle

class Stadium:
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def get_info(self):
        return f"Стадион: {self.name}, Вместимость: {self.capacity}, Локация: {self.location}"

    def increase_capacity(self, amount):
        self.capacity += amount
        print(f"Вместимость стадиона увеличена на {amount}. Новая вместимость: {self.capacity}")

class StadiumJSONAdapter:
    @staticmethod
    def to_json(stadium):
        return json.dumps({
            'name': stadium.name,
            'capacity': stadium.capacity,
            'location': stadium.location
        })

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        return Stadium(data['name'], data['capacity'], data['location'])

def save_stadium_pickle(stadium, filename):
    with open(filename, 'wb') as file:
        pickle.dump(stadium, file)

def load_stadium_pickle(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Пример использования
if __name__ == "__main__":
    # Создаем объект стадиона
    stadium = Stadium("Олимпийский", 50000, "Москва")
    print(stadium.get_info())

    # Увеличиваем вместимость
    stadium.increase_capacity(5000)

    # Упаковка в JSON
    json_data = StadiumJSONAdapter.to_json(stadium)
    print("JSON данные:", json_data)

    # Распаковка из JSON
    new_stadium = StadiumJSONAdapter.from_json(json_data)
    print(new_stadium.get_info())

    # Сохранение в файл с использованием Pickle
    save_stadium_pickle(stadium, 'stadium.pkl')

    # Загрузка из файла с использованием Pickle
    loaded_stadium = load_stadium_pickle('stadium.pkl')
    print(loaded_stadium.get_info())