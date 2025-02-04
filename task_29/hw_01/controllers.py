from models import Shoe

class ShoeController:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)
        print("Обувь добавлена:", shoe)

    def get_all_shoes(self):
        return self.shoes

    def get_shoe(self, index):
        if 0 <= index < len(self.shoes):
            return self.shoes[index]
        return None

    def delete_shoe(self, index):
        if 0 <= index < len(self.shoes):
            removed_shoe = self.shoes.pop(index)
            print("Обувь удалена:", removed_shoe)
            return removed_shoe
        return None