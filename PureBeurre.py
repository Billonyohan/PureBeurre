from tkinter import Button, Canvas, RIGHT, LEFT, PhotoImage, Label, N, S, E, W, Scrollbar
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import mysql.connector
from Constant import *
from SelectMysql import mysql_select
select = mysql_select()


class tkinterWindow:

    def second_frame(self, frame):
        label_category = tk.Label(frame, text="Catégories : ", bg="#9E9E9E").grid(row=0, column=0)
        self.combobox_category = ttk.Combobox(frame, values=select.select_category(), width=30)
        self.combobox_category.grid(row=0, column=1)
        label_food = tk.Label(frame, text="Aliments : ", bg="#9E9E9E").grid(row=2, column=0)
        label_subsitute = tk.Label(frame, text="Aliments à substituer :", bg="#9E9E9E").grid(row=0, column=5)
        button_choice_food = Button(frame, text="Valider", command=tkinterW.get_ingredients).grid(row=3, column=1)
        button_choice_category = Button(frame, text="Valider", command=tkinterW.get_category_food).grid(row=1, column=1)
        button_choice_subsitute = tk.Button(frame, text="Valider", command=tkinterW.get_substitute).grid(row=1, column=6)
        button_subsitute_food = tk.Button(frame, text="Substituer aliment", command=tkinterW.substitute_saved, bg="#FAFAFA").grid(row=28, column=5, sticky=W)
        button_subsitute = tk.Button(frame, text="Historique", command=tkinterW.scrollbar2, bg="#FAFAFA").grid(row=28, column=6, sticky=E)
        space = tk.Label(frame, text="            ", bg="#FFFFFF").grid(row=0, column=4)
        self.second_window.mainloop()

    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def scrollbar(self):
        self.second_window = tk.Tk()
        self.second_window.title("Database OpenFoodFact")
        self.second_window.configure(bg="#CECECE")
        self.second_window.geometry("950x650")
        canvas = tk.Canvas(self.second_window)
        self.frame = tk.Frame(canvas)
        vsb = tk.Scrollbar(self.second_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4, 4), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", lambda event, canvas=canvas: self.onFrameConfigure(canvas))
        self.second_frame(self.frame)
        self.second_window.mainloop()

    def get_category_food(self):
        self.get_index = self.combobox_category.current()
        self.get_index = self.get_index + 1
        self.get_index = str(self.get_index)
        self.combobox_food = ttk.Combobox(self.frame, values=select.select_food(self.get_index), width=30)
        self.combobox_food.grid(row=2, column=1)
        self.combobox_substitute = ttk.Combobox(self.frame, values=select.select_substitute(self.get_index), width=30)
        self.combobox_substitute.grid(row=0, column=6)

    def get_ingredients(self):
        self.get_index = int(self.get_index)
        if self.get_index == 1:
            self.get_index_food = self.combobox_food.current()
            self.get_index_food += 1
            self.get_index_food = str(self.get_index_food)
            label_ingredients = tk.Label(self.frame, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
            description_food = tk.Label(self.frame, text=select.ingredients_food(self.get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=0, rowspan=10, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=17, column=0, sticky=N+E+S+W)
            select_nutriscore_food = select.nutriscore_food(self.get_index_food)[0]
            if select_nutriscore_food == "a":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#88FE00").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "b":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#C6F700").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "c":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#F7D600").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "d":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#F7A500").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "e":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#F73200").grid(row=17, column=1, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=18, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Store", wraplength=350, bg="#C9DFDC").grid(row=19, column=0, columnspan=2, sticky=N+E+S+W)
            data_store_food = tk.Label(self.frame, text=select.store_food(self.get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=20, column=0, columnspan=2, sticky=N+S+E+W)
            space_column = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=21, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Link", wraplength=350, bg="#C9DFDC").grid(row=22, column=0, columnspan=2, sticky=N+E+S+W)
            data_link_susbtitute = tk.Label(self.frame, text=select.link_food(self.get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=23, column=0, columnspan=2, sticky=N+S+E+W)
            self.second_window.mainloop()
        elif self.get_index >= 2:
            self.get_index_food = self.combobox_food.current()
            self.get_index_food += 1
            for i in range(self.get_index - 1):
                self.get_index_food += 10
            self.get_index_food = str(self.get_index_food)
            label_ingredients = tk.Label(self.frame, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
            description_food = tk.Label(self.frame, text=select.ingredients_food(self.get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=0, rowspan=10, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=17, column=0, sticky=N+E+S+W)
            select_nutriscore_food = select.nutriscore_food(self.get_index_food)[0]
            if select_nutriscore_food == "a":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#88FE00").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "b":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#C6F700").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "c":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#F7D600").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "d":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#F7A500").grid(row=17, column=1, sticky=N+S+E+W)
            elif select_nutriscore_food == "e":
                nutriscore = tk.Label(self.frame, text=select_nutriscore_food, wraplength=350, bg="#F73200").grid(row=17, column=1, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=18, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Store", wraplength=350, bg="#C9DFDC").grid(row=19, column=0, columnspan=2, sticky=N+E+S+W)
            data_store_susbtitute = tk.Label(self.frame, text=select.store_food(self.get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=20, column=0, columnspan=2, sticky=N+S+E+W)
            space_column = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=21, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Link", wraplength=350, bg="#C9DFDC").grid(row=22, column=0, columnspan=2, sticky=N+E+S+W)
            tk.Label(self.frame, text=select.link_food(self.get_index_food)[0], wraplength=350, bg="#FAFAFA").grid(row=23, column=0, columnspan=2, sticky=N+S+E+W)
            self.second_window.mainloop()

    def get_substitute(self):
        self.get_index = int(self.get_index)
        idCategory = self.get_index
        if self.get_index == 1:
            self.get_index_substitute = self.combobox_substitute.current()
            self.get_index_substitute += 1
            self.get_index_substitute = str(self.get_index_substitute)
            label_ingredients = tk.Label(self.frame, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=5, columnspan=2, sticky=N+E+S+W)
            ingredients_substitute = tk.Label(self.frame, text=select.ingredients_substitute(self.get_index_substitute)[0], wraplength=350, bg="#FAFAFA")
            ingredients_substitute.grid(row=5, column=5, rowspan=10, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=17, column=5, sticky=N+E+S+W)
            select_nutriscore_substitute = select.nutriscore_substitute(self.get_index_substitute)[0]
            if select_nutriscore_substitute == "a":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#88FE00").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "b":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#C6F700").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "c":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#F7D600").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "d":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#F7A500").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "e":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#F73200").grid(row=17, column=6, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=18, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Store", wraplength=350, bg="#C9DFDC").grid(row=19, column=5, columnspan=2, sticky=N+E+S+W)
            store_substitute = tk.Label(self.frame, text=select.store_substitute(self.get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=20, column=5, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=21, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Link", wraplength=350, bg="#C9DFDC").grid(row=22, column=5, columnspan=2, sticky=N+E+S+W)
            link_substitute = tk.Label(self.frame, text=select.link_substitute(self.get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=23, column=5, columnspan=2, sticky=N+S+E+W)
            self.frame.mainloop()
        elif self.get_index >= 2:
            self.get_index_substitute = self.combobox_substitute.current()
            self.get_index_substitute += 1
            for i in range(self.get_index - 1):
                self.get_index_substitute += 25
            self.get_index_substitute = str(self.get_index_substitute)
            label_ingredients = tk.Label(self.frame, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=5, columnspan=2, sticky=N+E+S+W)
            ingredients_substitute = tk.Label(self.frame, text=select.ingredients_substitute(self.get_index_substitute)[0], wraplength=350, bg="#FAFAFA")
            ingredients_substitute.grid(row=5, column=5, rowspan=10, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=17, column=5, sticky=N+E+S+W)
            select_nutriscore_substitute = select.nutriscore_substitute(self.get_index_substitute)[0]
            if select_nutriscore_substitute == "a":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#88FE00").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "b":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#C6F700").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "c":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#F7D600").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "d":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#F7A500").grid(row=17, column=6, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "e":
                nutriscore_substitute = tk.Label(self.frame, text=select_nutriscore_substitute, wraplength=350, bg="#F73200").grid(row=17, column=6, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=18, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Store", wraplength=350, bg="#C9DFDC").grid(row=19, column=5, columnspan=2, sticky=N+E+S+W)
            store_substitute = tk.Label(self.frame, text=select.store_substitute(self.get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=20, column=5, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(self.frame, text="  ", wraplength=350, bg="#FAFAFA").grid(row=21, column=5, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame, text="Link", wraplength=350, bg="#C9DFDC").grid(row=22, column=5, columnspan=2, sticky=N+E+S+W)
            link_substitute = tk.Label(self.frame, text=select.link_substitute(self.get_index_substitute)[0], wraplength=350, bg="#FAFAFA").grid(row=23, column=5, columnspan=2, sticky=N+S+E+W)
            self.second_window.mainloop()

    def third_frame(self, frame2):
        self.combobox_substitute_save = ttk.Combobox(self.frame2, values=select.substitute_save(), width=40)
        self.combobox_substitute_save.grid(row=0, column=1)
        button_subsitute = tk.Button(self.frame2, text="Valider", command=self.substitute_food_saved, relief="solid", bg="#FEFEFE").grid(row=0, column=2)
        self.substitute_food_saved()
        self.third_window.mainloop()

    def onFrame2Configure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def scrollbar2(self):
        self.third_window = tk.Tk()
        self.third_window.title("Database OpenFoodFact")
        self.third_window.configure(bg="#CECECE")
        self.third_window.geometry("950x350")
        canvas = tk.Canvas(self.third_window)
        self.frame2 = tk.Frame(canvas)
        vsb = tk.Scrollbar(self.third_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4, 4), window=self.frame2, anchor="nw")
        self.frame2.bind("<Configure>", lambda event, canvas=canvas: self.onFrame2Configure(canvas))
        self.third_frame(self.frame2)
        self.third_window.mainloop()

    def substitute_saved(self):
        select.substitute_saved(self.get_index_substitute)
        select.food_saved(self.get_index_food)

    def substitute_food_saved(self):
        label_subsitute = tk.Label(self.frame2, text="Aliments : ", relief="solid", bg="#FEFEFE").grid(row=0, column=0)
        data_susbstitute = []
        connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
        index = self.combobox_substitute_save.current()
        index += 1
        index = str(index)
        if len(select.nutriscore_substitute_saved(index)) > 0:
            label_ingredients = tk.Label(self.frame2, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=1, column=0, columnspan=2, sticky=N+E+S+W)
            ingredients_substitute = tk.Label(self.frame2, text=select.ingredients_substitute_saved(index)[0], wraplength=350, bg="#FAFAFA")
            ingredients_substitute.grid(row=2, column=0, rowspan=10, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame2, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=13, column=0, sticky=N+E+S+W)
            select_nutriscore_substitute = select.nutriscore_substitute_saved(index)[0]
            if select_nutriscore_substitute == "a":
                nutriscore_substitute = tk.Label(self.frame2, text=select_nutriscore_substitute, wraplength=350, bg="#88FE00").grid(row=13, column=5, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "b":
                nutriscore_substitute = tk.Label(self.frame2, text=select_nutriscore_substitute, wraplength=350, bg="#C6F700").grid(row=13, column=5, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "c":
                nutriscore_substitute = tk.Label(self.frame2, text=select_nutriscore_substitute, wraplength=350, bg="#F7D600").grid(row=13, column=1, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "d":
                nutriscore_substitute = tk.Label(self.frame2, text=select_nutriscore_substitute, wraplength=350, bg="#F7A500").grid(row=13, column=1, sticky=N+S+E+W)
            elif select_nutriscore_substitute == "e":
                nutriscore_substitute = tk.Label(self.frame2, text=select_nutriscore_substitute, wraplength=350, bg="#F73200").grid(row=13, column=1, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame2, text="Store", wraplength=350, bg="#C9DFDC").grid(row=14, column=0, columnspan=2, sticky=N+E+S+W)
            store_substitute = tk.Label(self.frame2, text=select.store_substitute_saved(index)[0], wraplength=350, bg="#FAFAFA").grid(row=15, column=0, columnspan=2, sticky=N+S+E+W)
            space_column = tk.Label(self.frame2, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=0, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame2, text="Link", wraplength=350, bg="#C9DFDC").grid(row=17, column=0, columnspan=2, sticky=N+E+S+W)
            link_substitute = tk.Label(self.frame2, text=select.link_substitute_saved(index)[0], wraplength=350, bg="#FAFAFA").grid(row=18, column=0, columnspan=2, sticky=N+S+E+W)
            space = tk.Label(self.frame2, text="            ", bg="#CECECE"). grid(row=11, column=3)
            label_food = tk.Label(self.frame2, text=select.food_save(index)[0], bg="#9E9E9E").grid(row=0, column=4, columnspan=2, sticky=N+S+E+W)
            labelIngredients = tk.Label(self.frame2, text="Ingredients", wraplength=350, bg="#C9DFDC").grid(row=1, column=4, columnspan=2, sticky=N+E+S+W)
            description_food = tk.Label(self.frame2, text=select.ingredients_food_saved(index)[0], wraplength=350, bg="#FAFAFA").grid(row=2, column=4, rowspan=10, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame2, text="Nutriscore", wraplength=350, bg="#C9DFDC").grid(row=13, column=4, sticky=N+E+S+W)
            select_nutriscore_food = select.nutriscore_food_saved(index)[0]
            if select_nutriscore_food == "a":
                nutriscore_food = tk.Label(self.frame2, text=select_nutriscore_food, wraplength=350, bg="#88FE00").grid(row=13, column=5, sticky=N+S+E+W)
            elif select_nutriscore_food == "b":
                nutriscore_food = tk.Label(self.frame2, text=select_nutriscore_food, wraplength=350, bg="#C6F700").grid(row=13, column=5, sticky=N+S+E+W)
            elif select_nutriscore_food == "c":
                nutriscore_food = tk.Label(self.frame2, text=select_nutriscore_food, wraplength=350, bg="#F7D600").grid(row=13, column=5, sticky=N+S+E+W)
            elif select_nutriscore_food == "d":
                nutriscore_food = tk.Label(self.frame2, text=select_nutriscore_food, wraplength=350, bg="#F7A500").grid(row=13, column=5, sticky=N+S+E+W)
            elif select_nutriscore_food == "e":
                nutriscore_food = tk.Label(self.frame2, text=select_nutriscore_food, wraplength=350, bg="#F73200").grid(row=13, column=5, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame2, text="Store", wraplength=350, bg="#C9DFDC").grid(row=14, column=4, columnspan=2, sticky=N+E+S+W)
            store_food = tk.Label(self.frame2, text=select.store_food_saved(index)[0], wraplength=350, bg="#FAFAFA").grid(row=15, column=4, columnspan=2, sticky=N+S+E+W)
            space_column = tk.Label(self.frame2, text="  ", wraplength=350, bg="#FAFAFA").grid(row=16, column=4, columnspan=2, sticky=N+S+E+W)
            label_ingredients = tk.Label(self.frame2, text="Link", wraplength=350, bg="#C9DFDC").grid(row=17, column=4, columnspan=2, sticky=N+E+S+W)
            link_food = tk.Label(self.frame2, text=select.link_food_saved(index)[0], wraplength=350, bg="#FAFAFA").grid(row=18, column=4, columnspan=2, sticky=N+S+E+W)
        self.third_window.mainloop()


if __name__ == "__main__":
    # creation window
    window = tk.Tk()
    # format window
    window.title("Database OpenFoodFact")
    window.geometry("950x400")
    # creation title
    label_title = Label(window, text="Bienvenue dans la base de données OpenFoodFacts", font=("Helvetica", 40), fg="#41B77F").pack()
    # creation image
    width = 300
    height = 300
    image = PhotoImage(file="/Users/macbookair/Documents/GitHub/PureBeurre/PureBeurre/openfoodfacts-logo-fr-178x150.png")
    canvas = Canvas(window, width=width, height=height)
    canvas.create_image(width/2, height/2, image=image)
    canvas.pack()
    # creation button
    tkinterW = tkinterWindow()
    button_search = tk.Button(window, text="Trouver un aliment à remplacer", command=tkinterW.scrollbar).pack(side=LEFT, padx=100)
    button_historic = tk.Button(window, text="Retrouver mes aliments substitués", command=tkinterW.scrollbar2).pack(side=RIGHT, padx=100)
    window.mainloop()
