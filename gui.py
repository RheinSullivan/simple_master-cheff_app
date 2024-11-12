import tkinter as tk
from tkinter import messagebox
from recipe_manager import RecipeManager
from models import Recipe

class MasterCheffApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Master Cheff")
        self.recipe_manager = RecipeManager()
        self.build_gui()

    def build_gui(self):

        title_label = tk.Label(self.root, text="Master Cheff", font=("Arial", 16))
        title_label.pack(pady=10)
        
        add_recipe_button = tk.Button(self.root, text="Tambah Resep", command=self.add_recipe)
        add_recipe_button.pack(pady=5)
        
        self.recipe_listbox = tk.Listbox(self.root, width=50, height=20)
        self.recipe_listbox.pack(pady=10)
        self.load_recipes()

    def load_recipes(self):
        self.recipe_listbox.delete(0, tk.END)
        for recipe in self.recipe_manager.get_recipes():
            self.recipe_listbox.insert(tk.END, recipe[1]) 

    def add_recipe(self):

        add_window = tk.Toplevel(self.root)
        add_window.title("Input data resep")

        tk.Label(add_window, text="Nama:").grid(row=0, column=0)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Bahan:").grid(row=1, column=0)
        ingredients_entry = tk.Entry(add_window)
        ingredients_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Instruksi:").grid(row=2, column=0)
        instructions_entry = tk.Entry(add_window)
        instructions_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Kategori:").grid(row=3, column=0)
        category_entry = tk.Entry(add_window)
        category_entry.grid(row=3, column=1)

        tk.Label(add_window, text="Kesulitan:").grid(row=4, column=0)
        difficulty_entry = tk.Entry(add_window)
        difficulty_entry.grid(row=4, column=1)

        tk.Label(add_window, text="Durasi:").grid(row=5, column=0)
        duration_entry = tk.Entry(add_window)
        duration_entry.grid(row=5, column=1)

        def save_recipe():
            recipe = Recipe(
                name=name_entry.get(),
                ingredients=ingredients_entry.get(),
                instructions=instructions_entry.get(),
                category=category_entry.get(),
                difficulty=difficulty_entry.get(),
                duration=int(duration_entry.get())
            )
            self.recipe_manager.add_recipe(recipe)
            self.load_recipes()
            add_window.destroy()
            messagebox.showinfo("Sukses", "Resep berhasil ditambahkan!")

        save_button = tk.Button(add_window, text="Simpan", command=save_recipe)
        save_button.grid(row=6, columnspan=2)

    def run(self):
        self.root.mainloop()
