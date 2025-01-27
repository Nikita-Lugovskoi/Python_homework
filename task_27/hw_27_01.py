# 1.Создайте реализацию паттерна Builder на примере ремонтной бригады, 
# у вас должно быть 3 конкретных строителя и прораб (директор): 
# плиточник - производит: подготовка пола, укладка плитки; 
# отделочник - нанести шпаклевку, оштукатурить стены; 
# маляр - загрунтовать стену, покрасить стену. 
# прораб - директор у него именно по стройке 4 метода: сделать полы, выровнять стены, покрасить стены, работы под ключ .

class FloorTiler:
    def prepare_floor(self):
        print("Плиточник: Подготовка пола завершена.")

    def lay_tiles(self):
        print("Плиточник: Укладка плитки завершена.")


class Finisher:
    def apply_putty(self):
        print("Отделочник: Нанесение шпаклевки завершено.")

    def plaster_walls(self):
        print("Отделочник: Оштукатуривание стен завершено.")


class Painter:
    def prime_walls(self):
        print("Маляр: Загрунтование стен завершено.")

    def paint_walls(self):
        print("Маляр: Покраска стен завершена.")


class Foreman:
    def __init__(self):
        self.tiler = FloorTiler()
        self.finisher = Finisher()
        self.painter = Painter()

    def make_floors(self):
        self.tiler.prepare_floor()
        self.tiler.lay_tiles()

    def level_walls(self):
        self.finisher.apply_putty()
        self.finisher.plaster_walls()

    def paint_walls(self):
        self.painter.prime_walls()
        self.painter.paint_walls()

    def complete_work(self):
        print("Прораб: Все работы выполнены под ключ.")


if __name__ == "__main__":
    foreman = Foreman()
    foreman.make_floors()
    foreman.level_walls()
    foreman.paint_walls()
    foreman.complete_work()