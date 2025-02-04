from models import Recipe
from controllers import RecipeController
class RecipeView:
    @staticmethod
    def display_recipes(recipes):
        for recipe in recipes:
            print(f"Название: {recipe['title']}")
            print(f"Автор: {recipe['author']}")
            print(f"Тип: {recipe['type']}")
            print(f"Описание: {recipe['description']}")
            print(f"Ингредиенты: {', '.join(recipe['ingredients'])}")
            print(f"Кухня: {recipe['cuisine']}")
            if recipe['link']:
                print(f"Ссылка: {recipe['link']}")
            print("-" * 40)

    @staticmethod
    def display_recipe(recipe):
        if recipe:
            print(f"Название: {recipe['title']}")
            print(f"Автор: {recipe['author']}")
            print(f"Тип: {recipe['type']}")
            print(f"Описание: {recipe['description']}")
            print(f"Ингредиенты: {', '.join(recipe['ingredients'])}")
            print(f"Кухня: {recipe['cuisine']}")
            if recipe['link']:
                print(f"Ссылка: {recipe['link']}")
        else:
            print("Рецепт не найден.")
            
if __name__ == "__main__":
    controller = RecipeController()

    recipe1 = Recipe(
        title="Паста Карбонара",
        author="Итальянский шеф",
        recipe_type="Основное блюдо",
        description="Классическая итальянская паста с беконом и яйцом.",
        ingredients=["паста", "бекон", "яйцо", "сыр пармезан", "перец"],
        cuisine="Итальянская",
        link="https://www.youtube.com/watch?v=example"
    )

    recipe2 = Recipe(
        title="Борщ",
        author="Украинский шеф",
        recipe_type="Первое блюдо",
        description="Традиционный украинский суп с свеклой.",
        ingredients=["свекла", "капуста", "картофель", "морковь", "мясо"],
        cuisine="Украинская",
        link="https://www.youtube.com/watch?v=example"
    )

    # Добавляем рецепты в контроллер
    controller.add_recipe(recipe1)
    controller.add_recipe(recipe2)

    # Отображаем все рецепты
    print("Все рецепты:")
    RecipeView.display_recipes(controller.get_all_recipes())

    # Поиск рецепта по названию
    print("\nПоиск рецепта 'Борщ':")
    found_recipe = controller.find_recipe_by_title("Борщ")
    RecipeView.display_recipe(found_recipe)