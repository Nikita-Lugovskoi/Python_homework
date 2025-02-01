# Создайте реализацию паттерна Command. Протестируйте работу созданного класса (нет не тесты, создайте необходимые объекты и примените к ним необходимые методы) .

from abc import ABC, abstractmethod

# Интерфейс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретная команда для включения света
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Конкретная команда для выключения света
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Получатель
class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")

# Инициатор
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
        else:
            print("Команда не установлена")

# Тестирование
if __name__ == "__main__":
    # Создаем получателя
    light = Light()

    # Создаем команды
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Создаем инициатор
    remote = RemoteControl()

    # Включаем свет
    remote.set_command(light_on)
    remote.press_button() 

    # Выключаем свет
    remote.set_command(light_off)
    remote.press_button()  