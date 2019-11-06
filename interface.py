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
second_window.geometry("920x400")

def get_ingredients():
	global comboExample1
	global get_index

	get_index_food = comboExample1.current()
	get_index_food = get_index_food + 1
	get_index_food = str(get_index_food)
	cursor.execute("SELECT ingredients FROM Food WHERE idCategory ="+get_index)
	data_ingredients = cursor.fetchall()
	data_ingredients = [d[0] for d in data_ingredients]
	description_food = tk.Label(second_window, text= data_ingredients, wraplength=450, bg = "#99A4A2").grid(row=3, column=0, columnspan=3)

def get_category_food_substitute():
	global comboExample1
	global get_index
	get_index = comboExample.current()
	get_index = get_index + 1
	get_index = str(get_index)
	cursor.execute("SELECT food FROM Food WHERE idCategory ="+get_index)
	data_food = cursor.fetchall()
	data_food = [d[0] for d in data_food]
	comboExample1 = ttk.Combobox(second_window, values=data_food, width=30)
	comboExample1.grid(row=1, column=1)
	button_choice_food = Button(second_window, text="Valider", command=get_ingredients).grid(row=1, column=2)

labelCategory = tk.Label(second_window, text = "Catégories : ", bg = "#FAFAFA").grid(row=0, column=0)
connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
cursor = connexion_data_base.cursor()
cursor.execute(" SELECT category FROM Category")
data_category = cursor.fetchall()
data_category = [d[0] for d in data_category] 
comboExample = ttk.Combobox(second_window, values=data_category, width=30)
comboExample.grid(row=0, column=1)
button_choice_category = Button(second_window, text="Valider", command=get_category_food_substitute).grid(row=0, column=2)
labelFood = tk.Label(second_window, text = "Aliments : ", bg = "#FAFAFA").grid(row=1, column=0)



second_window.mainloop()
