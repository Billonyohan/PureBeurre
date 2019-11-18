from tkinter import *
import tkinter as tk
from tkinter import tix, ttk
from tkinter.ttk import Combobox
import mysql.connector
from Constant import *

index_food_save = []
index_substitute_save = []
def substitute_food():
	global index_food_save
	global index_substitute_save

	third_window = tk.Tk()
	third_window.configure(bg="#CECECE")
	third_window.geometry("950x350")
	button_subsitute2 = tk.Button(third_window, text="Valider", command=substitute_food, relief="solid", bg="#FEFEFE").grid(row=0, column=2)
	second_window = tk.Tk()
	second_window.destroy()	
	label_subsitute = tk.Label(third_window, text = "Aliments : ", relief="solid", bg="#FEFEFE").grid(row=0, column=0)
	data_susbstitute = []
	for i in range(len(index_substitute_save)):
		connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
		cursor = connexion_data_base.cursor()
		cursor.execute("SELECT substitute FROM Substitute WHERE id="+index_substitute_save[i])
		data_susbstitute2 = cursor.fetchall()
		data_susbstitute += [d[0] for d in data_susbstitute2]
		comboExample = ttk.Combobox(third_window, values=data_susbstitute, width=40)
		comboExample.grid(row=0, column=1)
		cursor.execute("SELECT ingredients FROM substitute WHERE id ="+index_substitute_save[i])
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(third_window, text= "Ingredients", wraplength=350, bg="#C9DFDC").grid(row=2, column=1, sticky=N+E+S+W)
		data_ingredients_susbstitute = tk.Label(third_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=3, column=1, sticky=N+S+E+W)
		description_susbtitute = tk.Label(third_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=4, column=1, sticky=N+S+E+W)
		cursor.execute("SELECT store FROM substitute WHERE id ="+index_substitute_save[i])
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(third_window, text= "Store", wraplength=350, bg="#C9DFDC").grid(row=5, column=1, sticky=N+E+S+W)
		data_store_susbtitute = tk.Label(third_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=6, column=1, sticky=N+S+E+W)
		space_column= tk.Label(third_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=7, column=1, sticky=N+S+E+W)
		cursor.execute("SELECT link FROM substitute WHERE id ="+index_substitute_save[i])
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(third_window, text= "Link", wraplength=350, bg="#C9DFDC").grid(row=8, column=1, sticky=N+E+S+W)
		data_link_susbtitute = tk.Label(third_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=9, column=1, sticky=N+S+E+W)
		space = tk.Label(third_window, text="            ", bg="#CECECE"). grid(row=0, column=3)
		get_index_food = comboExample.current()
		index_food_save = index_food_save[get_index_food]
		cursor.execute("SELECT food FROM Food WHERE id ="+index_food_save)
		data_food = cursor.fetchall()
		data_food = [d[0] for d in data_food]
		label_food = tk.Label(third_window, text= data_food[0], bg="#9E9E9E").grid(row=1, column=4, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT ingredients FROM Food WHERE id ="+index_food_save)
		data_ingredients = cursor.fetchall()
		data_ingredients = [d[0] for d in data_ingredients]
		labelIngredients = tk.Label(third_window, text= "Ingredients", wraplength=350, bg="#C9DFDC").grid(row=2, column=4, columnspan=2, sticky=N+E+S+W)
		description_food = tk.Label(third_window, text= data_ingredients[0], wraplength=350, bg="#FAFAFA").grid(row=3, column=4, rowspan=10, columnspan=2, sticky=N+S+E+W)


def saved_substitute():
	global	get_index_food
	global get_index_substitute
	global index_substitute_save
	global	index_food_save
	index_food_save.append(get_index_food)
	index_substitute_save.append(get_index_substitute)


def get_substitute():
	global get_index
	global comboExample2
	global get_index_substitute
	get_index = int(get_index)
	if get_index == 1:
		get_index_substitute = comboExample2.current()
		get_index_substitute += 1
		get_index_substitute = str(get_index_substitute)
		cursor.execute("SELECT ingredients FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(second_window, text= "Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=5, columnspan=2, sticky=N+E+S+W)
		data_ingredients_susbstitute = tk.Label(second_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=5, columnspan=2, sticky=N+S+E+W)
		description_susbtitute = tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=6, column=5, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT store FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(second_window, text= "Store", wraplength=350, bg="#C9DFDC").grid(row=7, column=5, columnspan=2, sticky=N+E+S+W)
		data_store_susbtitute = tk.Label(second_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=8, column=5, columnspan=2, sticky=N+S+E+W)
		space_column= tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=9, column=5, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT link FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(second_window, text= "Link", wraplength=350, bg="#C9DFDC").grid(row=10, column=5, columnspan=2, sticky=N+E+S+W)
		data_link_susbtitute = tk.Label(second_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=11, column=5, columnspan=2, sticky=N+S+E+W)
		second_window.mainloop()

	elif get_index >= 2:
		get_index_substitute = comboExample2.current()
		get_index_substitute += 1
		for i in range(get_index - 1):
			get_index_substitute += 20
		get_index_substitute = str(get_index_substitute)
		cursor.execute("SELECT ingredients FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(second_window, text= "Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=5, columnspan=2, sticky=N+E+S+W)
		data_ingredients_susbstitute = tk.Label(second_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=5, columnspan=2, sticky=N+S+E+W)
		description_susbtitute = tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=6, column=5, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT store FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(second_window, text= "Store", wraplength=350, bg="#C9DFDC").grid(row=7, column=5, columnspan=2, sticky=N+E+S+W)
		data_store_susbtitute = tk.Label(second_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=8, column=5, columnspan=2, sticky=N+S+E+W)
		space_column= tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=9, column=5, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT link FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		label_ingredients = tk.Label(second_window, text= "Link", wraplength=350, bg="#C9DFDC").grid(row=10, column=5, columnspan=2, sticky=N+E+S+W)
		data_link_susbtitute = tk.Label(second_window, text= data_susbstitute[0], wraplength=350, bg="#FAFAFA").grid(row=11, column=5, columnspan=2, sticky=N+S+E+W)
		second_window.mainloop()

def get_ingredients():
	global comboExample1
	global get_index
	global get_index_food
	get_index = int(get_index)
	if get_index == 1:
		get_index_food = comboExample1.current()
		get_index_food += 1
		get_index_food = str(get_index_food)
		cursor.execute("SELECT ingredients FROM Food WHERE id ="+get_index_food)
		data_ingredients = cursor.fetchall()
		data_ingredients = [d[0] for d in data_ingredients]
		label_ingredients = tk.Label(second_window, text= "Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
		description_food = tk.Label(second_window, text= data_ingredients[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=0,rowspan=15, columnspan=2, sticky=N+S+E+W)
		second_window.mainloop()
	elif get_index >= 2:
		get_index_food = comboExample1.current()
		get_index_food += 1
		for i in range(get_index - 1):
			get_index_food += 10
		get_index_food = str(get_index_food)
		cursor.execute("SELECT ingredients FROM Food WHERE id ="+get_index_food)
		data_ingredients = cursor.fetchall()
		data_ingredients = [d[0] for d in data_ingredients]
		label_ingredients = tk.Label(second_window, text= "Ingredients", wraplength=350, bg="#C9DFDC").grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
		description_food = tk.Label(second_window, text= data_ingredients[0], wraplength=350, bg="#FAFAFA").grid(row=5, column=0, rowspan=15, columnspan=2, sticky=N+S+E+W)
		second_window.mainloop()


def get_category_food():
	global comboExample1
	global get_index
	global comboExample2
	get_index = comboExample.current()
	get_index = get_index + 1
	get_index = str(get_index)
	cursor.execute("SELECT food FROM Food WHERE idCategory ="+get_index)
	data_food = cursor.fetchall()
	data_food = [d[0] for d in data_food]
	comboExample1 = ttk.Combobox(second_window, values=data_food, width=30)
	comboExample1.grid(row=2, column=1)
	cursor.execute("SELECT substitute FROM Substitute WHERE idCategory="+get_index)
	data_susbstitute = cursor.fetchall()
	data_susbstitute = [d[0] for d in data_susbstitute]
	comboExample2 = ttk.Combobox(second_window, values=data_susbstitute, width=30)
	comboExample2.grid(row=0, column=6)


connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
cursor = connexion_data_base.cursor()
cursor.execute(" SELECT category FROM Category")
data_category = cursor.fetchall()
data_category = [d[0] for d in data_category] 

#creation window
window = tk.Tk()
#format window
window.title("Database OpenFoodFact") 
window.geometry("950x400")
#creation title
label_title = Label(window, text="Bienvenue dans la base de donnée OpenFoodFacts", font=("Helvetica", 40), fg="#41B77F").pack()
#creation image
width = 300
height = 300
image = PhotoImage(file="/Users/macbookair/Documents/GitHub/PureBeurre/PureBeurre/openfoodfacts-logo-fr-178x150.png")
canvas = Canvas(window, width=width, height=height)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()
#creation button
button_connect = tk.Button(window, text="Trouver un aliment à remplacer", command=window.destroy).pack(side=LEFT, padx = 100)
button_connect2 = tk.Button(window, text="Retrouver mes aliments substitués", command=substitute_food).pack(side=RIGHT, padx = 100)
# print window
window.mainloop()
second_window = tk.Tk()
second_window.configure(bg="#CECECE")
second_window.geometry("950x650")

labelCategory = tk.Label(second_window, text = "Catégories : ", relief="solid", bg="#FEFEFE").grid(row=0, column=0)
comboExample = ttk.Combobox(second_window, values=data_category, width=30)
comboExample.grid(row=0, column=1)
button_choice_food = Button(second_window, text="Valider", command=get_ingredients).grid(row=3, column=1)
button_choice_category = Button(second_window, text="Valider", command=get_category_food).grid(row=1, column=1)
button_choice_subsitute = tk.Button(second_window, text="Valider", command=get_substitute).grid(row=1, column=6)
labelFood = tk.Label(second_window, text = "Aliments : ", relief="solid", bg="#FEFEFE").grid(row=2, column=0)
label_subsitute = tk.Label(second_window, text="Aliments à substituer :", relief="solid", bg="#FEFEFE").grid(row=0, column=5)
button_subsitute_food = tk.Button(second_window, text="Substituer aliment", command=saved_substitute, bg="#FAFAFA").grid(row=16, column=5, sticky="w")
button_subsitute = tk.Button(second_window, text="Historique", command=substitute_food, bg="#FAFAFA").grid(row=16, column=6, sticky="e")
space = tk.Label(second_window, text="            ", bg="#CECECE"). grid(row=0, column=4)
second_window.mainloop()
