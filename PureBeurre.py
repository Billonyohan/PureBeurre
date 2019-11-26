from tkinter import Button, Canvas, RIGHT, LEFT, PhotoImage, Label, N, S, E, W
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import mysql.connector
from Constant import *
from SelectMysql import mysql_select
select = mysql_select()


class tkinterWindow:

    def substitute_food_save():
        global index_food_save
        global index_substitute_save
        third_window = tk.Tk()
        third_window.configure(bg="#CECECE")
        third_window.geometry("950x350")
        label_subsitute = tk.Label(third_window, text="Aliments : ", relief="solid", bg="#FEFEFE").grid(row=0, column=0)
        data_susbstitute = []
        connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
        combobox_substitute_save = ttk.Combobox(third_window, values=select.substitute_save(), width=40)
        combobox_substitute_save.grid(row=0, column=1)
        index = combobox_substitute_save.current()
        index = str(index)
        label_ingredients = tk.Label(third_window, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=1, column=0, columnspan=2, sticky=N+E+S+W)
        ingredients_substitute = tk.Label(third_window, text=select.ingredients_substitute_saved(index)[0], wraplength=350, bg="#FAFAFA")
        ingredients_substitute.grid(row=2, column=0, rowspan=10, columnspan=2, sticky=N+S+E+W)
        label_ingredients = tk.Label(third_window, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=13, column=0, sticky=N+E+S+W)
        select_nutriscore_substitute = select.nutriscore_substitute_saved(index)[0]
        label_nutriscore_substitute = tk.Label(third_window, text=select_nutriscore_substitute[0], wraplength=350, bg="#88FE00").grid(row=13, column=1, sticky=N+S+E+W)
        if select_nutriscore_substitute == "a":
            nutriscore_substitute = label_nutriscore_substitute
        elif select_nutriscore_substitute == "b":
            nutriscore_substitute = label_nutriscore_substitute
        elif select_nutriscore == "c":
            select_nutriscore_substitute = label_nutriscore_substitute
        elif select_nutriscore == "d":
            select_nutriscore_substitute = label_nutriscore_substitute
        elif select_nutriscore == "e":
            select_nutriscore_substitute = label_nutriscore_substitute
        label_ingredients = tk.Label(third_window, text="Store", wraplength=350, bg="#C9DFDC").grid(row=14, column=0, columnspan=2, sticky=N+E+S+W)
        store_substitute = tk.Label(third_window, text=select.store_susbstitute(index)[0], wraplength=350, bg="#FAFAFA").grid(row=15, column=0, columnspan=2, sticky=N+S+E+W)
        space_column = tk.Label(third_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=0, columnspan=2, sticky=N+S+E+W)
        label_ingredients = tk.Label(third_window, text="Link", wraplength=350, bg="#C9DFDC").grid(row=17, column=0, columnspan=2, sticky=N+E+S+W)
        link_substitute = tk.Label(third_window, text=select.link_substitute(index)[0], wraplength=350, bg="#FAFAFA").grid(row=18, column=0, columnspan=2, sticky=N+S+E+W)
        space = tk.Label(third_window, text="            ", bg="#CECECE"). grid(row=11, column=3)
        label_food = tk.Label(third_window, text=select.food_saved(index)[0], bg="#9E9E9E").grid(row=0, column=4, columnspan=2, sticky=N+S+E+W)
        labelIngredients = tk.Label(third_window, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=1, column=4, columnspan=2, sticky=N+E+S+W)
        description_food = tk.Label(third_window, text=select.ingredients_food_saved(index)[0], wraplength=350, bg="#FAFAFA").grid(row=2, column=4, rowspan=10, columnspan=2, sticky=N+S+E+W)
        label_ingredients = tk.Label(third_window, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=13, column=4, sticky=N+E+S+W)
        select_nutriscore_food = select.nutriscore_food_saved(index)[0]
        label_nutriscore_food = nutriscore_food = tk.Label(third_window, text=select_nutriscore_food[0], wraplength=350, bg="#88FE00").grid(row=13, column=5, sticky=N+S+E+W)
        if select_nutriscore_food == "a":
            nutriscore_food = label_nutriscore_food
        elif select_nutriscore_food == "b":
            nutriscore_food = label_nutriscore_food
        elif select_nutriscore_food == "c":
            nutriscore_food = label_nutriscore_food
        elif select_nutriscore_food == "d":
            nutriscore_food = label_nutriscore_food
        elif select_nutriscore_food == "e":
            nutriscore_food = label_nutriscore_food
        label_ingredients = tk.Label(third_window, text="Store", wraplength=350, bg="#C9DFDC").grid(row=14, column=4, columnspan=2, sticky=N+E+S+W)
        store_food = tk.Label(third_window, text=select.store_food_save(index)[0], wraplength=350, bg="#FAFAFA").grid(row=15, column=4, columnspan=2, sticky=N+S+E+W)
        space_column = tk.Label(third_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=4, columnspan=2, sticky=N+S+E+W)
        label_ingredients = tk.Label(third_window, text="Link", wraplength=350, bg="#C9DFDC").grid(row=17, column=4, columnspan=2, sticky=N+E+S+W)
        link_food = tk.Label(third_window, text=select.link_food_saved(index)[0], wraplength=350, bg="#FAFAFA").grid(row=18, column=4, columnspan=2, sticky=N+S+E+W)
        button_subsitute = tk.Button(third_window, text="Valider", command=substitute_food_save, relief="solid", bg="#FEFEFE").grid(row=0, column=2)

    def saved_substitute():
        global get_index_food
        global get_index_substitute
        select.substitute_saved(get_index_substitute)
        select.food_saved(get_index_food)

    def get_substitute():
        global get_index
        global combobox_substitute
        global get_index_substitute
        get_index = int(get_index)
        idCategory = get_index
        if get_index == 1:
            get_index_substitute = combobox_substitute.current()
            get_index_substitute += 1
            get_index_substitute = str(get_index_substitute)
            label_ingredients = tk.Label(second_window, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=5, columnspan=2, sticky=N+E+S+W)
            ingredients_substitute = tk.Label(second_window, text=select.ingredients_substitute(get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=5, rowspan=14, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=20, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=21, column=5, sticky=N+E+S+W)
            select_nutriscore_substitute = select.nutriscore_substitute(get_index_substitute)[0]
            label_nutriscore_substitute = tk.Label(second_window, text=select.nutriscore_substitute(get_index_substitute)[0], wraplength=350, bg="#88FE00").grid(row=21, column=6, sticky=N+S+E+W)
            if select_nutriscore_substitute == "a":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "b":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "c":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "d":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "e":
                nutriscore_substitute = label_nutriscore_substitute
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=22, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Store", wraplength=350, bg="#C9DFDC").grid(row=23, column=5, columnspan=2, sticky=N+E+S+W)
            store_substitute = tk.Label(second_window, text=select.store_substitute(get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=24, column=5, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=25, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Link", wraplength=350, bg="#C9DFDC").grid(row=26, column=5, columnspan=2, sticky=N+E+S+W)
            link_substitute = tk.Label(second_window, text=select.link_substitute(get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=27, column=5, columnspan=2, sticky=N+S+E+W)
            second_window.mainloop()
        elif get_index >= 2:
            get_index_substitute = combobox_substitute.current()
            get_index_substitute += 1
            for i in range(get_index - 1):
                get_index_substitute += 25
            get_index_substitute = str(get_index_substitute)
            label_ingredients = tk.Label(second_window, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=5, columnspan=2, sticky=N+E+S+W)
            ingredients_susstitute = tk.Label(second_window, text=select.ingredients_substitute(get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=5, rowspan=15, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=20, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=21, column=5, sticky=N+E+S+W)
            select_nutriscore_substitute = select.nutriscore_substitute(get_index_substitute)[0]
            label_nutriscore_substitute = tk.Label(second_window, text=select.nutriscore_substitute(get_index_substitute)[0], wraplength=350, bg="#88FE00").grid(row=21, column=6, sticky=N+S+E+W)
            if select_nutriscore_substitute == "a":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "b":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "c":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "d":
                nutriscore_substitute = label_nutriscore_substitute
            elif select_nutriscore_substitute == "e":
                nutriscore_substitute = label_nutriscore_substitute
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=22, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Store", wraplength=350, bg="#C9DFDC").grid(row=23, column=5, columnspan=2, sticky=N+E+S+W)
            store_substitute = tk.Label(second_window, text=select.store_substitute(get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=24, column=5, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=25, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Link", wraplength=350, bg="#C9DFDC").grid(row=26, column=5, columnspan=2, sticky=N+E+S+W)
            link_substitute = tk.Label(second_window, text=select.link_substitute(get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=27, column=5, columnspan=2, sticky=N+S+E+W)
            second_window.mainloop()

    def get_ingredients():
        global combobox_food
        global get_index
        global get_index_food
        get_index = int(get_index)
        if get_index == 1:
            get_index_food = combobox_food.current()
            get_index_food += 1
            get_index_food = str(get_index_food)
            label_ingredients = tk.Label(second_window, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
            description_food = tk.Label(second_window, text=select.ingredients_food(get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=0, rowspan=15, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=20, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=21, column=0, sticky=N+E+S+W)
            select_nutriscore_food = select.nutriscore_food(get_index_food)[0]
            label_nutriscore_food = tk.Label(second_window, text=select.nutriscore_food(get_index_food)[0], wraplength=350, bg="#88FE00").grid(row=21, column=1, sticky=N+S+E+W)
            if select_nutriscore_food == "a":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "b":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "c":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "d":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "e":
                nutriscore = label_nutriscore_food
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=22, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Store", wraplength=350, bg="#C9DFDC").grid(row=23, column=0, columnspan=2, sticky=N+E+S+W)
            data_store_food = tk.Label(second_window, text=select.store_food(get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=24, column=0, columnspan=2, sticky=N+S+E+W)
            space_column = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=25, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Link", wraplength=350, bg="#C9DFDC").grid(row=26, column=0, columnspan=2, sticky=N+E+S+W)
            data_link_susbtitute = tk.Label(second_window, text=select.link_food(get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=27, column=0, columnspan=2, sticky=N+S+E+W)
            second_window.mainloop()
        elif get_index >= 2:
            get_index_food = combobox_food.current()
            get_index_food += 1
            for i in range(get_index - 1):
                get_index_food += 10
            get_index_food = str(get_index_food)
            label_ingredients = tk.Label(second_window, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
            description_food = tk.Label(second_window, text=select.ingredients_food(get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=0, rowspan=15, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=20, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=21, column=0, sticky=N+E+S+W)
            select_nutriscore_food = select.nutriscore_food(get_index_food)[0]
            label_nutriscore_food = tk.Label(second_window, text=select.nutriscore_food(get_index_food)[0], wraplength=350, bg="#88FE00").grid(row=21, column=1, sticky=N+S+E+W)
            if select_nutriscore_food == "a":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "b":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "c":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "d":
                nutriscore = label_nutriscore_food
            elif select_nutriscore_food == "e":
                nutriscore = label_nutriscore_food
            space = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=22, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Store", wraplength=350, bg="#C9DFDC").grid(row=23, column=0, columnspan=2, sticky=N+E+S+W)
            data_store_susbtitute = tk.Label(second_window, text=select.store_food(get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=24, column=0, columnspan=2, sticky=N+S+E+W)
            space_column = tk.Label(second_window, text="  ", wraplength=350, bg="#FAFAFA").grid(row=25, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(second_window, text="Link", wraplength=350, bg="#C9DFDC").grid(row=26, column=0, columnspan=2, sticky=N+E+S+W)
            tk.Label(second_window, text=select.link_food(get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=27, column=0, columnspan=2, sticky=N+S+E+W)
            second_window.mainloop()

    def get_category_food():
        global combobox_category
        global combobox_food
        global combobox_substitute
        global second_window
        global get_index
        get_index = combobox_category.current()
        get_index = get_index + 1
        get_index = str(get_index)
        combobox_food = ttk.Combobox(second_window, values=select.select_food(get_index), width=30)
        combobox_food.grid(row=2, column=1)
        combobox_substitute = ttk.Combobox(second_window, values=select.select_substitute(get_index), width=30)
        combobox_substitute.grid(row=0, column=6)


    if __name__ == "__main__":
        global combobox_category    
        global second_window
        # creation window
        window = tk.Tk()
        # format window
        window.title("Database OpenFoodFact")
        window.geometry("950x400")
        # creation title
        label_title = Label(window, text="Bienvenue dans la base de donnée OpenFoodFacts", font=("Helvetica", 40), fg="#41B77F").pack()
        # creation image
        width = 300
        height = 300
        image = PhotoImage(file="/Users/macbookair/Documents/GitHub/PureBeurre/PureBeurre/openfoodfacts-logo-fr-178x150.png")
        canvas = Canvas(window, width=width, height=height)
        canvas.create_image(width/2, height/2, image=image)
        canvas.pack()
        # creation button
        button_connect = tk.Button(window, text="Trouver un aliment à remplacer", command=window.destroy).pack(side=LEFT, padx=100)
        button_connect2 = tk.Button(window, text="Retrouver mes aliments substitués", command=substitute_food_save).pack(side=RIGHT, padx=100)
        # print window
        window.mainloop()
        second_window = tk.Tk()
        second_window.configure(bg="#CECECE")
        second_window.geometry("950x650")
        label_category = tk.Label(second_window, text="Catégories : ", bg="#9E9E9E").grid(row=0, column=0)
        combobox_category = ttk.Combobox(second_window, values=select.select_category(), width=30)
        combobox_category.grid(row=0, column=1)
        label_food = tk.Label(second_window, text="Aliments : ", bg="#9E9E9E").grid(row=2, column=0)
        label_subsitute = tk.Label(second_window, text="Aliments à substituer :", bg="#9E9E9E").grid(row=0, column=5)
        button_choice_food = Button(second_window, text="Valider", command=get_ingredients).grid(row=3, column=1)
        button_choice_category = Button(second_window, text="Valider", command=get_category_food).grid(row=1, column=1)
        button_choice_subsitute = tk.Button(second_window, text="Valider", command=get_substitute).grid(row=1, column=6)
        button_subsitute_food = tk.Button(second_window, text="Substituer aliment", command=saved_substitute, bg="#FAFAFA").grid(row=28, column=5, sticky=W)
        button_subsitute = tk.Button(second_window, text="Historique", command=substitute_food_save, bg="#FAFAFA").grid(row=28, column=6, sticky=E)
        space = tk.Label(second_window, text="            ", bg="#CECECE"). grid(row=0, column=4)
        second_window.mainloop()

