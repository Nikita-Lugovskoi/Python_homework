# На занятии я вам показал реализацию паттерна MVC на бэкенде для модели MarksModel. 
# Вам нужно сделать аналогичную рабочую реализацию для модели Обувь, именно как бэкенд реализация. 
# Необходимо хранить следующую информацию: 
# тип обуви; ✓мужская, ✓женская; 
# вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.); 
# цвет; 
# цена; 
# производитель; 
# размер. 
# Создайте необходимые методы для этого класса. 
# Реализуйте паттерн MVC для класса Обувь и код для использования модели, контроллера и представления.


class Shoe:
    def __init__(self, shoe_type, shoe_kind, color, price, manufacturer, size):
        self.shoe_type = shoe_type  
        self.shoe_kind = shoe_kind  
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __repr__(self):
        return (f"Обувь(тип={self.shoe_type}, вид={self.shoe_kind}, цвет={self.color}, "
                f"цена={self.price}, производитель={self.manufacturer}, размер={self.size})")