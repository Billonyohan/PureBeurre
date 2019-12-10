'''Mysql modyle and module constant from my file contant.py who import the data connexion'''
import mysql.connector
from constant import *


class MysqlSelect:
    '''Class that manage the selection in my database Mysql and the insertion line 77/85 of data saved'''
    def __init__(self):
        self.connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD,
                                                           host=MYSQL_HOST, database=MYSQL_DATABASE)
        self.cursor = self.connexion_data_base.cursor()

    def select_category(self):
        '''Method for select category of my database'''
        self.cursor.execute("SELECT category FROM Category")
        self.data_category = self.cursor.fetchall()
        self.data_category = [d[0] for d in self.data_category]
        return self.data_category

    def select_food(self, id_category):
        '''Method for select food of my database'''
        self.cursor.execute("SELECT food FROM Food WHERE id_category ="+id_category)
        self.data_food = self.cursor.fetchall()
        self.data_food = [d[0] for d in self.data_food]
        return self.data_food

    def ingredients_food(self, index):
        '''Method for select ingredients food of my database'''
        self.cursor.execute("SELECT ingredients FROM Food WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_food(self, index):
        '''Method for select nutriscore food of my database'''
        self.cursor.execute("SELECT nutriscore FROM Food WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_food(self, index):
        '''Method for select store food of my database'''
        self.cursor.execute("SELECT store FROM food WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_food(self, index):
        '''Method for select link food of my database'''
        self.cursor.execute("SELECT link FROM food WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link

    def select_substitute(self, id_category):
        '''Method for select substitute of my database'''
        self.cursor.execute("SELECT substitute FROM Substitute WHERE id_category="+id_category)
        self.data_susbstitute = self.cursor.fetchall()
        self.data_susbstitute = [d[0] for d in self.data_susbstitute]
        return self.data_susbstitute

    def ingredients_substitute(self, index):
        '''Method for select ingredients substitute of my database'''
        self.cursor.execute("SELECT ingredients FROM substitute WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_substitute(self, index):
        '''Method for select nutriscore substitute of my database'''
        self.cursor.execute("SELECT nutriscore FROM Substitute WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_substitute(self, index):
        '''Method for select store substitute of my database'''
        self.cursor.execute("SELECT store FROM substitute WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_substitute(self, index):
        '''Method for select link substitute of my database'''
        self.cursor.execute("SELECT link FROM substitute WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link

    def substitute_saved(self, id_substitute):
        '''Method for insert substitute saved in my database'''
        add_sub = (""" INSERT INTO SubstituteSaved (substitute, ingredients, nutriscore, store, link)
        SELECT substitute, ingredients, nutriscore, store, link FROM Substitute WHERE id ="""+id_substitute)
        self.cursor.execute(add_sub)
        self.connexion_data_base.commit()

    def food_saved(self, id_food):
        '''Method for insert food saved in my database'''
        add_fo = ("""INSERT INTO FoodSaved (food, ingredients, nutriscore, store, link)
            SELECT food, ingredients, nutriscore, store, link FROM Food WHERE id ="""+id_food)
        self.cursor.execute(add_fo)
        self.connexion_data_base.commit()

    def food_save(self, index):
        '''Method for select food saved of my database'''
        self.cursor.execute("SELECT food FROM FoodSaved WHERE id="+index)
        self.data_food = self.cursor.fetchall()
        self.data_food = [d[0] for d in self.data_food]
        return self.data_food

    def ingredients_food_saved(self, index):
        '''Method for select ingredients food saved of my database'''
        self.cursor.execute("SELECT ingredients FROM FoodSaved WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_food_saved(self, index):
        '''Method for select nutriscore food saved of my database'''
        self.cursor.execute("SELECT nutriscore FROM FoodSaved WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_food_saved(self, index):
        '''Method for select store food saved of my database'''
        self.cursor.execute("SELECT store FROM FoodSaved WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_food_saved(self, index):
        '''Method for select link food saved of my database'''
        self.cursor.execute("SELECT link FROM FoodSaved WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link

    def substitute_save(self):
        '''Method for select  substitute saved of my database'''
        self.cursor.execute("SELECT substitute FROM SubstituteSaved")
        self.data_susbstitute = self.cursor.fetchall()
        self.data_susbstitute = [d[0] for d in self.data_susbstitute]
        return self.data_susbstitute

    def ingredients_substitute_saved(self, index):
        '''Method for select  ingredients substitute saved of my database'''
        self.cursor.execute("SELECT ingredients FROM SubstituteSaved WHERE id ="+index)
        self.data_ingredients = self.cursor.fetchall()
        self.data_ingredients = [d[0] for d in self.data_ingredients]
        return self.data_ingredients

    def nutriscore_substitute_saved(self, index):
        '''Method for select  nutriscore substitute saved of my database'''
        self.cursor.execute("SELECT nutriscore FROM SubstituteSaved WHERE id="+index)
        self.data_nutriscore = self.cursor.fetchall()
        self.data_nutriscore = [d[0] for d in self.data_nutriscore]
        return self.data_nutriscore

    def store_substitute_saved(self, index):
        '''Method for select store substitute saved of my database'''
        self.cursor.execute("SELECT store FROM SubstituteSaved WHERE id ="+index)
        self.data_store = self.cursor.fetchall()
        self.data_store = [d[0] for d in self.data_store]
        return self.data_store

    def link_substitute_saved(self, index):
        '''Method for select link substitute saved of my database'''
        self.cursor.execute("SELECT link FROM SubstituteSaved WHERE id ="+index)
        self.data_link = self.cursor.fetchall()
        self.data_link = [d[0] for d in self.data_link]
        return self.data_link
