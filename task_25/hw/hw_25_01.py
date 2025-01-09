# Задание 1
import pickle

class CountryCapitalDictionary:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        """Добавление страны и её столицы."""
        self.data[country] = capital
        print(f"Добавлено: {country} - {capital}")

    def remove_country(self, country):
        """Удаление страны и её столицы."""
        if country in self.data:
            del self.data[country]
            print(f"Удалено: {country}")
        else:
            print(f"Страна {country} не найдена.")

    def find_capital(self, country):
        """Поиск столицы по названию страны."""
        return self.data.get(country, "Страна не найдена.")

    def edit_country(self, country, new_capital):
        """Редактирование столицы для существующей страны."""
        if country in self.data:
            self.data[country] = new_capital
            print(f"Обновлено: {country} - {new_capital}")
        else:
            print(f"Страна {country} не найдена.")

    def save_data(self, filename):
        """Сохранение данных в файл."""
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)
            print(f"Данные сохранены в {filename}")

    def load_data(self, filename):
        """Загрузка данных из файла."""
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
                print(f"Данные загружены из {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

# Пример использования
if __name__ == "__main__":
    country_capital_dict = CountryCapitalDictionary()
    
    # Добавление данных
    country_capital_dict.add_country("Россия", "Москва")
    country_capital_dict.add_country("США", "Вашингтон")
    
    # Поиск данных
    print(country_capital_dict.find_capital("Россия"))  
    print(country_capital_dict.find_capital("Канада"))  
    
    # Редактирование данных
    country_capital_dict.edit_country("США", "Вашингтон, округ Колумбия")
    
    # Удаление данных
    country_capital_dict.remove_country("Россия")
    
    # Сохранение данных
    country_capital_dict.save_data("countries.pkl")
    
    # Загрузка данных
    country_capital_dict.load_data("countries.pkl")

# Задание 2
import pickle

class MusicLibrary:
    def __init__(self):
        self.library = {}

    def add_band(self, band_name, albums):
        """Добавление группы и её альбомов."""
        self.library[band_name] = albums
        print(f"Группа '{band_name}' добавлена с альбомами: {albums}")

    def remove_band(self, band_name):
        """Удаление группы."""
        if band_name in self.library:
            del self.library[band_name]
            print(f"Группа '{band_name}' удалена.")
        else:
            print(f"Группа '{band_name}' не найдена.")

    def find_band(self, band_name):
        """Поиск группы и её альбомов."""
        if band_name in self.library:
            return self.library[band_name]
        else:
            print(f"Группа '{band_name}' не найдена.")
            return None

    def edit_band(self, band_name, new_albums):
        """Редактирование альбомов группы."""
        if band_name in self.library:
            self.library[band_name] = new_albums
            print(f"Альбомы группы '{band_name}' обновлены на: {new_albums}")
        else:
            print(f"Группа '{band_name}' не найдена.")

    def save_to_file(self, filename):
        """Сохранение данных в файл."""
        with open(filename, 'wb') as file:
            pickle.dump(self.library, file)
        print(f"Данные сохранены в файл '{filename}'.")

    def load_from_file(self, filename):
        """Загрузка данных из файла."""
        try:
            with open(filename, 'rb') as file:
                self.library = pickle.load(file)
            print(f"Данные загружены из файла '{filename}'.")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

# Пример использования
if __name__ == "__main__":
    music_library = MusicLibrary()
    
    # Добавление данных
    music_library.add_band("The Beatles", ["Abbey Road", "Let It Be"])
    music_library.add_band("Nirvana", ["Nevermind", "In Utero"])
    
    # Поиск данных
    print(music_library.find_band("The Beatles"))
    
    # Редактирование данных
    music_library.edit_band("Nirvana", ["MTV Unplugged in New York"])
    
    # Удаление данных
    music_library.remove_band("The Beatles")
    
    # Сохранение данных
    music_library.save_to_file("music_library.pkl")
    
    # Загрузка данных
    music_library.load_from_file("music_library.pkl")