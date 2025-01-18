"""Реализовать класс «Автомобиль» у которого будет
минимум 3 атрибута и 2 метода, добавьте
возможность упаковки и распаковки данных с
использованием json и pickle, для json метод упаковки
на ваш выбор."""

import json
import pickle


class Automobile:
    def __init__(self, make, model, year):
        self.make = make  # Производитель
        self.model = model  # Модель
        self.year = year  # Год выпуска

    def start_engine(self):
        return f"{self.make} {self.model} engine started."

    def stop_engine(self):
        return f"{self.make} {self.model} engine stopped."


class JsonHandler:
    @staticmethod
    def to_json(obj):
        """Упаковка данных объекта в JSON формат."""
        return json.dumps(obj.__dict__)

    @staticmethod
    def from_json(json_data, cls):
        """Распаковка данных из JSON формата в объект класса."""
        data = json.loads(json_data)
        return cls(**data)


class PickleHandler:
    @staticmethod
    def to_pickle(obj):
        """Упаковка данных объекта с использованием pickle."""
        return pickle.dumps(obj)

    @staticmethod
    def from_pickle(pickle_data, cls):
        """Распаковка данных из pickle формата в объект класса."""
        return pickle.loads(pickle_data)


# Пример использования
if __name__ == "__main__":
    car = Automobile("Toyota", "Camry", 2020)
    
    # Упаковка в JSON
    json_data = JsonHandler.to_json(car)
    print("JSON:", json_data)

    # Распаковка из JSON
    new_car_from_json = JsonHandler.from_json(json_data, Automobile)
    print("Car from JSON:", new_car_from_json.__dict__)

    # Упаковка с использованием pickle
    pickle_data = PickleHandler.to_pickle(car)
    print("Pickle data:", pickle_data)

    # Распаковка из pickle
    new_car_from_pickle = PickleHandler.from_pickle(pickle_data, Automobile)
    print("Car from Pickle:", new_car_from_pickle.__dict__)