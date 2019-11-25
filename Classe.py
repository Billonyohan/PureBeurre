# -*- coding: utf-8 -*-
import mysql.connector
import requests
from Constant import *


class OpenFoodFact:
    def __init__(self):
        self.connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)
        self.data_base = dataBaseMySql()
        self.data_base.delete_table()
        self.data_base.create_data_base()
        self.get_category()
        self.get_food()
        self.get_substitute()

    def get_category(self):
        '''get category from API's openfoodfacts'''
        resp_category = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_category_json = resp_category.json()
        data_tags_category = data_category_json.get('tags')
        data_name_category = [d.get('name') for d in data_tags_category]
        for i in range(10):
            self.data_base.insert_data_category(data_name_category[i])

    def get_food(self):
        for i in range(1, 11):
            nb_init_category = i
            nb_food = 10
            cursor = self.connexion_data_base.cursor()
            nb_category = str(nb_init_category)
            select_category = ("SELECT category FROM Category WHERE idCategory = "+nb_category)
            cursor.execute(select_category)
            category_saved = str(cursor.fetchone()[0])
            parameters = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': '{}'.format(category_saved),
            'sort_by': 'unique_scans_n',
            'page_size': '{}'.format(nb_food),
            'countries': 'France',
            'json': 1,
            'page': 1
            }
            r_food = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=parameters)
            food_json = r_food.json()
            data_food = food_json.get('products')
            food_id = ("SELECT idCategory FROM Category WHERE idCategory = "+nb_category)
            cursor.execute(food_id)
            food_id_saved = cursor.fetchone()[0]

            for j in range(nb_food):
                food = [d.get('product_name_fr') for d in data_food]
                ingredients = [d.get('ingredients_text_fr') for d in data_food]
                nutriscore = [d.get('nutriscore_grade') for d in data_food]
                store = [d.get('stores') for d in data_food]
                link = [d.get('link') for d in data_food]
                self.data_base.insert_data_food(nb_category, food[j], ingredients[j], nutriscore[j], store[j], link[j])

    def get_substitute(self):

        for i in range(1, 11):
            nb_init_substitute = i
            nb_substitute = 35
            cursor = self.connexion_data_base.cursor()
            nb_category = str(nb_init_substitute)
            select_category = ("SELECT category FROM Category WHERE idCategory = "+nb_category)
            cursor.execute(select_category)
            substitute_saved = str(cursor.fetchone()[0])
            parameters = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': '{}'.format(substitute_saved),
            'sort_by': 'unique_scans_n',
            'page_size': '{}'.format(nb_substitute),
            'countries': 'France',
            'json': 1,
            'page': 1
            }
            request_substitute = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=parameters)
            subsitute_json = request_substitute.json()
            data_substitute = subsitute_json.get('products')
            substitute_id = ("SELECT idCategory FROM Category WHERE idCategory = "+nb_category)
            cursor.execute(substitute_id)
            food_id_saved = cursor.fetchone()[0]

            for j in range(10, 35):
                food = [d.get('product_name_fr') for d in data_substitute]
                ingredients = [d.get('ingredients_text_fr') for d in data_substitute]
                nutriscore = [d.get('nutriscore_grade') for d in data_substitute]
                store = [d.get('stores') for d in data_substitute]
                link = [d.get('link') for d in data_substitute]
                self.data_base.insert_substitute_food(nb_category, food[j], ingredients[j], nutriscore[j], store[j], link[j])


class dataBaseMySql:
    def __init__(self):
        self.connexion_data_base = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=MYSQL_DATABASE)

    def delete_table(self):
        self.cursor = self.connexion_data_base.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS Food")
        self.cursor.execute("DROP TABLE IF EXISTS Substitute")
        self.cursor.execute("DROP TABLE IF EXISTS Category")
        self.cursor.execute("DROP TABLE IF EXISTS SubstituteSaved")
        self.cursor.execute("DROP TABLE IF EXISTS FoodSaved")
        self.connexion_data_base.commit()

    def create_data_base(self):
        self.cursor = self.connexion_data_base.cursor()
        self.cursor.execute("""
            CREATE TABLE Category (
                idCategory int(15) NOT NULL AUTO_INCREMENT,
                category varchar(100) NOT NULL,
                PRIMARY KEY (idCategory)
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                """)

        self.cursor.execute("""
            CREATE TABLE Food (
                id int NOT NULL AUTO_INCREMENT,
                idCategory int(15) DEFAULT NULL,
                food varchar(400) NOT NULL,
                ingredients varchar(5000),
                nutriscore varchar(10) DEFAULT NULL,
                store varchar(1000) DEFAULT NULL,
                link varchar(1000) DEFAULT NULL,
                PRIMARY KEY (id)
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                """)

        self.cursor.execute("""
            CREATE TABLE Substitute (
                id int(11) NOT NULL AUTO_INCREMENT,
                idCategory int(15) DEFAULT NULL,
                substitute varchar(100) DEFAULT NULL,
                ingredients varchar(5000) DEFAULT NULL,
                nutriscore varchar(10) DEFAULT NULL,
                store varchar(1000) DEFAULT NULL,
                link varchar(1000) DEFAULT NULL,
                PRIMARY KEY (id)
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                """)

        self.cursor.execute("""
            CREATE TABLE SubstituteSaved (
                id int(11) NOT NULL AUTO_INCREMENT,
                substitute varchar(100) DEFAULT NULL,
                ingredients varchar(5000) DEFAULT NULL,
                nutriscore varchar(10) DEFAULT NULL,
                store varchar(1000) DEFAULT NULL,
                link varchar(1000) DEFAULT NULL,
                PRIMARY KEY (id)
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                """)

        self.cursor.execute("""
            CREATE TABLE FoodSaved (
                id int(11) NOT NULL AUTO_INCREMENT,
                food varchar(400) NOT NULL,
                ingredients varchar(5000),
                nutriscore varchar(10) DEFAULT NULL,
                store varchar(1000) DEFAULT NULL,
                link varchar(1000) DEFAULT NULL,
                PRIMARY KEY (id)
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                """)

        self.connexion_data_base.commit()
        self.cursor.close()

    def insert_data_category(self, category):
        self.cursor = self.connexion_data_base.cursor()
        add_category = (""" INSERT INTO Category (category)
                            VALUES("{name_category}")""".format(name_category=category))
        self.cursor.execute(add_category)
        self.connexion_data_base.commit()
        self.cursor.close()
    def insert_data_food(self, idCategory, food, ingredients, nutriscore, store, link):
        self.cursor = self.connexion_data_base.cursor()
        add_food = (""" INSERT INTO Food (idCategory, food, ingredients, nutriscore, store, link)
                        VALUES("{cat_save}", "{name_food}", "{nb_ingredients}", "{nutri_score}", "{nb_store}", "{product_link}")""".format(cat_save=idCategory, name_food=food, nb_ingredients=ingredients, nutri_score=nutriscore, nb_store=store, product_link=link))
        self.cursor.execute(add_food)
        self.connexion_data_base.commit()
        self.cursor.close()

    def insert_substitute_food(self, idCategory, food, ingredients, nutriscore, store, link):
        self.cursor = self.connexion_data_base.cursor()
        add_substitute = (""" INSERT INTO Substitute (idCategory, substitute, ingredients, nutriscore,  store, link)
                            VALUES("{category_save}", "{name_food}", "{nb_ingredients}", "{nutri_score}", "{nb_store}", "{product_link}")""".format(category_save=idCategory, name_food=food, nb_ingredients=ingredients, nutri_score=nutriscore, nb_store=store, product_link=link))
        self.cursor.execute(add_substitute)
        self.connexion_data_base.commit()
        self.cursor.close()


create_data_base = OpenFoodFact()
