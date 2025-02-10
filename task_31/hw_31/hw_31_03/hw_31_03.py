# Создайте класс Фильм. Необходимо хранить следующую
# информацию:
# название фильма;
# жанр;
# режиссер;
# год выпуска;
# длительность;
# студия
# актеры: ФИО, роль.
# Реализуйте паттерн MVC для класса Фильм и код для
# использования модели, контроллера и представления

class Film:
    def __init__(self, title, genre, director, year, duration, studio):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = []  # Список актеров

    def add_actor(self, name, role):
        self.actors.append({'name': name, 'role': role})

    def get_info(self):
        info = f"Название: {self.title}\n" \
               f"Жанр: {self.genre}\n" \
               f"Режиссер: {self.director}\n" \
               f"Год выпуска: {self.year}\n" \
               f"Длительность: {self.duration} мин\n" \
               f"Студия: {self.studio}\n" \
               f"Актеры:\n"
        for actor in self.actors:
            info += f"  {actor['name']} - {actor['role']}\n"
        return info


class FilmController:
    def __init__(self, film):
        self.film = film

    def add_actor(self, name, role):
        self.film.add_actor(name, role)

    def get_film_info(self):
        return self.film.get_info()
    

class FilmView:
    @staticmethod
    def display_film_info(info):
        print(info)
        
        
if __name__ == "__main__":
    # Создаем экземпляр модели
    film = Film("Властелин колец: Братство кольца", "Фэнтези", "Питер Джексон", 2001, 178, "New Line Cinema")

    # Создаем контроллер
    controller = FilmController(film)

    # Добавляем актеров
    controller.add_actor("Элайджа Вуд", "Фродо Бэггинс")
    controller.add_actor("Иэн Маккеллен", "Гэндальф")
    controller.add_actor("Лив Тайлер", "Арвен")

    # Получаем информацию о фильме
    film_info = controller.get_film_info()

    # Создаем представление и отображаем информацию
    view = FilmView()
    view.display_film_info(film_info)