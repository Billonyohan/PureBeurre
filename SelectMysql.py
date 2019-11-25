import mysql.connector
from Constant import *


class mysql_select:
    def __init__(self):
        self.connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
        self.cursor = self.connexion_data_base.cursor()

    def select_category(self):
        self.cursor.execute("SELECT category FROM Category")
        self.data_category = self.cursor.fetchall()
        self.data_category = [d[0] for d in self.data_category]
        return self.data_category

    def select_food(self, idCategory):
        self.cursor.execute("SELECT food FROM Food WHERE idCategory ="+idCategory)
        self.data_food = self.cursor.fetchall()
        self.data_food = [d[0] for d in self.data_food]
        return self.data_food

    def ingredients_food(self, index):
        self.cursor.execute("SELECT ingredients FROM Food WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_food(self, index):
        self.cursor.execute("SELECT nutriscore FROM Food WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_food(self, index):
        self.cursor.execute("SELECT store FROM food WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_food(self, index):
        self.cursor.execute("SELECT link FROM food WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link

    def select_substitute(self, idCategory):
        self.cursor.execute("SELECT substitute FROM Substitute WHERE idCategory="+idCategory)
        self.data_susbstitute = self.cursor.fetchall()
        self.data_susbstitute = [d[0] for d in self.data_susbstitute]
        return self.data_susbstitute

    def ingredients_substitute(self, index):
        self.cursor.execute("SELECT ingredients FROM substitute WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_substitute(self, index):
        self.cursor.execute("SELECT nutriscore FROM Substitute WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_substitute(self, index):
        self.cursor.execute("SELECT store FROM substitute WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_substitute(self, index):
        self.cursor.execute("SELECT link FROM substitute WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link

    def substitute_saved(self, idSubstitute):
        add_sub = (" INSERT INTO SubstituteSaved (substitute, ingredients, nutriscore, store, link) SELECT substitute, ingredients, nutriscore, store, link FROM Substitute WHERE id ="+idSubstitute)
        self.cursor.execute(add_sub)
        self.connexion_data_base.commit()

    def food_saved(self, idFood):
        add_fo = ("INSERT INTO FoodSaved (food, ingredients, nutriscore, store, link) SELECT food, ingredients, nutriscore, store, link FROM Food WHERE id ="+idFood)
        self.cursor.execute(add_fo)
        self.connexion_data_base.commit()

    def food_save(self, index):
        self.cursor.execute("SELECT food FROM FoodSaved WHERE id="+index)
        self.data_food = self.cursor.fetchall()
        self.data_food = [d[0] for d in self.data_food]
        return self.data_food

    def ingredients_food_saved(self, index):
        self.cursor.execute("SELECT ingredients FROM FoodSaved WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_food_saved(self, index):
        self.cursor.execute("SELECT nutriscore FROM FoodSaved WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_food_saved(self, index):
        self.cursor.execute("SELECT store FROM FoodSaved WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_food_saved(self, index):
        self.cursor.execute("SELECT link FROM FoodSaved WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link

    def substitute_save(self):
        self.cursor.execute("SELECT substitute FROM SubstituteSaved")
        self.data_susbstitute = self.cursor.fetchall()
        self.data_susbstitute = [d[0] for d in self.data_susbstitute]
        return self.data_susbstitute

    def ingredients_substitute_saved(self, index):
        self.cursor.execute("SELECT ingredients FROM SubstituteSaved WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_substitute_saved(self, index):
        self.cursor.execute("SELECT nutriscore FROM SubstituteSaved WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_substitute_saved(self, index):
        self.cursor.execute("SELECT store FROM SubstituteSaved WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_substitute_saved(self, index):
        self.cursor.execute("SELECT link FROM SubstituteSaved WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link
