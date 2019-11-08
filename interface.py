from tkinter import *
import tkinter as tk
from tkinter import tix, ttk
from tkinter.ttk import Combobox
import mysql.connector
from Constant import *


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
button_connect2 = tk.Button(window, text="Retrouver mes aliments substitués").pack(side=RIGHT, padx = 100)
# print window
window.mainloop()


second_window = tk.Tk()
second_window.configure(bg="#CECECE")
second_window.geometry("950x350")


def get_substitute():
	global get_index
	global comboExample
	get_index = int(get_index)
	if get_index == 1:
		get_index_substitute = comboExample.current()
		get_index_substitute += 1
		get_index_substitute = str(get_index_substitute)
		cursor.execute("SELECT ingredients FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		data_susbstitute = tk.Label(second_window, text= data_susbstitute, wraplength=350, bg="#FAFAFA").grid(row=4, column=6, columnspan=2, sticky=N+S+E+W)
		description_susbtitute = tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=5, column=6, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT store FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		description_susbtitute = tk.Label(second_window, text= data_susbstitute, wraplength=350, bg="#FAFAFA").grid(row=6, column=6, columnspan=2, sticky=N+S+E+W)
		description_susbtitute = tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=7, column=6, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT link FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		description_susbtitute = tk.Label(second_window, text= data_susbstitute, wraplength=350, bg="#FAFAFA").grid(row=8, column=6, columnspan=2, sticky=N+S+E+W)
		second_window.mainloop()
	elif get_index >= 2:
		get_index_substitute = comboExample.current()
		get_index_substitute += 1
		for i in range(get_index - 1):
			get_index_substitute += 5
		get_index_substitute = str(get_index_substitute)
		cursor.execute("SELECT ingredients FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		data_susbstitute = tk.Label(second_window, text= data_susbstitute, wraplength=350, bg="#FAFAFA").grid(row=4, column=6, columnspan=2, sticky=N+S+E+W)
		description_susbtitute = tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=5, column=6, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT store FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		description_susbtitute = tk.Label(second_window, text= data_susbstitute, wraplength=350, bg="#FAFAFA").grid(row=6, column=6, columnspan=2, sticky=N+S+E+W)
		description_susbtitute = tk.Label(second_window, text= "  ", wraplength=350, bg="#FAFAFA").grid(row=7, column=6, columnspan=2, sticky=N+S+E+W)
		cursor.execute("SELECT link FROM substitute WHERE id ="+get_index_substitute)
		data_susbstitute = cursor.fetchall()
		data_susbstitute = [d[0] for d in data_susbstitute]
		description_susbtitute = tk.Label(second_window, text= data_susbstitute, wraplength=350, bg="#FAFAFA").grid(row=8, column=6, columnspan=2, sticky=N+S+E+W)
		second_window.mainloop()


def get_ingredients():
	global comboExample1
	global get_index
	get_index = int(get_index)
	if get_index == 1:
		get_index_food = comboExample1.current()
		get_index_food += 1
		get_index_food = str(get_index_food)
		cursor.execute("SELECT ingredients FROM Food WHERE id ="+get_index_food)
		data_ingredients = cursor.fetchall()
		data_ingredients = [d[0] for d in data_ingredients]
		description_food = tk.Label(second_window, text= data_ingredients, wraplength=350, bg="#FAFAFA").grid(row=4, column=0, rowspan=15, columnspan=2, sticky=N+S+E+W)
		second_window.mainloop()
	elif get_index >= 2:
		get_index_food = comboExample1.current()
		get_index_food += 1
		for i in range(get_index - 1):
			get_index_food += 5
		get_index_food = str(get_index_food)
		cursor.execute("SELECT ingredients FROM Food WHERE id ="+get_index_food)
		data_ingredients = cursor.fetchall()
		data_ingredients = [d[0] for d in data_ingredients]
		description_food = tk.Label(second_window, text= data_ingredients, wraplength=350, bg="#FAFAFA").grid(row=4, column=0, rowspan=15, columnspan=2)
		second_window.mainloop()


def get_category_food():
	global comboExample1
	global get_index
	get_index = comboExample.current()
	get_index = get_index + 1
	get_index = str(get_index)
	cursor.execute("SELECT food FROM Food WHERE idCategory ="+get_index)
	data_food = cursor.fetchall()
	data_food = [d[0] for d in data_food]
	comboExample1 = ttk.Combobox(second_window, values=data_food, width=30)
	comboExample1.grid(row=2, column=1)
	button_choice_food = Button(second_window, text="Valider", command=get_ingredients).grid(row=3, column=1)

	cursor.execute("SELECT substitute FROM Substitute WHERE idCategory="+get_index)
	data_susbstitute = cursor.fetchall()
	data_susbstitute = [d[0] for d in data_susbstitute]
	comboExample2 = ttk.Combobox(second_window, values=data_susbstitute, width=30)
	comboExample2.grid(row=0, column=6)
	button_choice_subsitute = tk.Button(second_window, text="Valider", command=get_substitute).grid(row=1, column=6)

labelCategory = tk.Label(second_window, text = "Catégories : ", bg="#9E9E9E").grid(row=0, column=0)
connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
cursor = connexion_data_base.cursor()
cursor.execute(" SELECT category FROM Category")
data_category = cursor.fetchall()
data_category = [d[0] for d in data_category] 
comboExample = ttk.Combobox(second_window, values=data_category, width=30)
comboExample.grid(row=0, column=1)
button_choice_category = Button(second_window, text="Valider", command=get_category_food).grid(row=1, column=1)
labelFood = tk.Label(second_window, text = "Aliments : ", bg="#9E9E9E").grid(row=2, column=0)
label_subsitute = tk.Label(second_window, text="Aliments à substituer :", bg="#9E9E9E").grid(row=0, column=5)
button_subsitute = tk.Button(second_window, text="Substituer aliment", bg="#FAFAFA").grid(row=16, column=6)
space = tk.Label(second_window, text="            ", bg="#CECECE"). grid(row=0, column=4)

second_window.mainloop()




