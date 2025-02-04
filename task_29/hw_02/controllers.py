class RecipeController:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_all_recipes(self):
        return [recipe.get_recipe_info() for recipe in self.recipes]

    def find_recipe_by_title(self, title):
        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                return recipe.get_recipe_info()
        return None