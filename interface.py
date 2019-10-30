from tkinter import *
import tkinter as tk
from tkinter import tix, ttk
import mysql.connector


#creation window
window = tk.Tk()

#format window
window.title("Database OpenFoodFact") 
window.geometry("950x400")

lst = ["1", "2"]

def __inti__(self):
	second_window()

def second_window():
	second_window = tk.Toplevel(window, bg = "#FAFAFA")
	second_window.geometry("920x400")
	labelCategory = tk.Label(second_window, text = "Catégories : ", bg = "#FAFAFA").grid(row=0, column=1)
	MYSQL_USER = 'yohan'
	MYSQL_HOST = 'localhost'
	MYSQL_PWD = 'logitech'
	MYSQL_DATABASE = 'OpenFoodFact'
	connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
	cursor = connexion_data_base.cursor()
	cursor.execute(" SELECT category FROM Category")
	data = cursor.fetchall()
	data = [d[0] for d in data] 
	comboExample = ttk.Combobox(second_window, values=data, width=30).grid(row=1, column=1, padx=50, pady=10)
	cursor.execute(" SELECT food FROM Food")
	food = str(cursor.fetchall())
	listbox = Listbox(second_window).grid(row=2, column=2)
	for i in range(11):
		listbox.insert(food)
	cursor.close()
	#labelDescription = tk.Label(second_window, text = "Description")
	second_window.mainloop()


#creation title
label_title = Label(window, text="Bienvenue dans la base de donnée OpenFoodFacts", font=("Helvetica", 40), fg="#41B77F").pack()

#creation image
width = 300
height = 300
image = PhotoImage(file="/Users/macbookair/Documents/Projet_5/PureBeurre/openfoodfacts-logo-fr-178x150.png")
canvas = Canvas(window, width=width, height=height)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()

#creation button
button_connect = tk.Button(window, text="Trouver un aliment à remplacer", command=second_window).pack(side=LEFT, padx = 100)
button_connect2 = tk.Button(window, text="Retrouver mes aliments substitués").pack(side=RIGHT, padx = 100)

# print window
window.mainloop()



