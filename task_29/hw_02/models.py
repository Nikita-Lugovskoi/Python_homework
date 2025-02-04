# Создайте модель Рецепт и реализуйте его по паттерну
# MVC именно как бэкенд реализацию. Необходимо
# хранить следующую информацию:
# название рецепта;
# автор рецепта;
# тип рецепта (первое, второе блюдо и т.д.);
# текстовое описание рецепта;
# список ингредиентов;
# название кухни (итальянская, французская,
# украинская и т.д.).
# *дополнительно ссылка на данный рецепт на youtube
# или в google
# Создайте необходимые методы для этого класса.
# Реализуйте паттерн MVC для класса Рецепт и код для
# использования модели, контроллера и представления.

class Recipe:
    def __init__(self, title, author, recipe_type, description, ingredients, cuisine, link=None):
        self.title = title
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.ingredients = ingredients 
        self.cuisine = cuisine
        self.link = link

    def get_recipe_info(self):
        return {
            "title": self.title,
            "author": self.author,
            "type": self.recipe_type,
            "description": self.description,
            "ingredients": self.ingredients,
            "cuisine": self.cuisine,
            "link": self.link
        }

    def __str__(self):
        return f"{self.title} by {self.author} ({self.recipe_type})"
    

