class Component:
    def __init__(self, name):
        self.name = name

class PowerSupply(Component):
    def __init__(self, power):
        super().__init__("Блок питания")
        self.power = power

    def supply_voltage(self):
        print(f"{self.name} подает напряжение {self.power} В")

class Motherboard(Component):
    def __init__(self, chipset):
        super().__init__("Материнская плата")
        self.chipset = chipset
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def redistribute_voltage(self, power_supply):
        print(f"{self.name} перераспределяет напряжение от {power_supply.name}")
        for component in self.components:
            component.supply_voltage(power_supply.power)

class CPU(Component):
    def __init__(self, frequency, cores):
        super().__init__("Центральный процессор")
        self.frequency = frequency
        self.cores = cores
        self.turbo_mode = False

    def activate_turbo_mode(self):
        self.turbo_mode = True
        print(f"{self.name} активировал турбо режим")

    def supply_voltage(self, power):
        print(f"{self.name} получил напряжение {power} В")

class RAM(Component):
    def __init__(self, capacity, frequency):
        super().__init__("Оперативная память")
        self.capacity = capacity
        self.frequency = frequency
        self.data = []

    def load_data(self, data):
        self.data.append(data)
        print(f"{self.name} загрузил данные {data}")

    def unload_data(self):
        if self.data:
            data = self.data.pop(0)
            print(f"{self.name} выгрузил данные {data}")
        else:
            print(f"{self.name} не имеет данных для выгрузки")

    def supply_voltage(self, power):
        print(f"{self.name} получил напряжение {power} В")

class SSD(Component):
    def __init__(self, capacity):
        super().__init__("SSD накопитель")
        self.capacity = capacity
        self.data = []

    def save_data(self, data):
        self.data.append(data)
        print(f"{self.name} сохранил данные {data}")

    def delete_data(self):
        if self.data:
            data = self.data.pop(0)
            print(f"{self.name} удалил данные {data}")
        else:
            print(f"{self.name} не имеет данных для удаления")

    def supply_voltage(self, power):
        print(f"{self.name} получил напряжение {power} В")

class VideoCard(Component):
    def __init__(self, model, capacity):
        super().__init__("Видеокарта")
        self.model = model
        self.capacity = capacity

    def output_image(self):
        print(f"{self.name} выводит изображение на экран")

    def supply_voltage(self, power):
        print(f"{self.name} получил напряжение {power} В")

class Computer(Motherboard, PowerSupply):
    def __init__(self, chipset, power):
        Motherboard.__init__(self, chipset)
        PowerSupply.__init__(self, power)

    def assemble(self):
        print("Компьютер собран")

    def start(self):
        print("Компьютер запущен")
        self.supply_voltage()
        self.redistribute_voltage(self)

# Создание компонентов
cpu = CPU(3.2, 8)
ram = RAM(16, 3200)
ssd = SSD(512)
video_card = VideoCard("NVIDIA GeForce GTX 1660", 6)

# Создание компьютера
computer = Computer("Intel Z390", 650)

# Добавление компонентов в компьютер
computer.add_component(cpu)
computer.add_component(ram)
computer.add_component(ssd)
computer.add_component(video_card)

# Собрать компьютер
computer.assemble()

# Запустить компьютер
computer.start()

# Активировать турбо режим процессора
cpu.activate_turbo_mode()

# Загрузить данные в оперативную память
ram.load_data("Данные 1")
ram.load_data("Данные 2")

# Выгрузить данные из оперативной памяти
ram.unload_data()

# Сохранить данные на SSD накопителе
ssd.save_data("Данные 3")

# Удалить данные из SSD накопителя
ssd.delete_data()

# Вывести изображение на экран видеокартой
video_card.output_image()