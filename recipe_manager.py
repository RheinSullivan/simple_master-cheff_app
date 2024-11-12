from database import Database
from models import Recipe

class RecipeManager:
    def __init__(self):
        self.db = Database()

    def add_recipe(self, recipe):
        query = """
        INSERT INTO recipes (name, ingredients, instructions, category, difficulty, duration)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (recipe.name, recipe.ingredients, recipe.instructions,
                                      recipe.category, recipe.difficulty, recipe.duration))

    def get_recipes(self, category=None):
        query = "SELECT * FROM recipes"
        if category:
            query += " WHERE category = ?"
            return self.db.execute_query(query, (category,)).fetchall()
        return self.db.execute_query(query).fetchall()

    def delete_recipe(self, recipe_id):
        query = "DELETE FROM recipes WHERE id = ?"
        self.db.execute_query(query, (recipe_id,))

    def close(self):
        self.db.close()
