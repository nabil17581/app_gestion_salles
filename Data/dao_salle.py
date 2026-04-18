import mysql.connector
import json

from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("./data/config.json","r",encoding="utf-8") as f:
            config=json.load(f)
        connection = mysql.connector.connect(
            host = config["host"],
            user = config["user"],
            password = config["password"],
            database = config["database"])
        return connection
    def add_data(self,salle):
        con = self.get_connection()
        cursor = con.cursor()
        sql = "INSERT INTO salle VALUES (%s,%s,%s,%s)"
        values = (salle.code,salle.description,salle.categorie,salle.capacite)
        cursor.execute(sql, values)
        print("Ajout d'une nouvelle salle réussit")
        con.commit()
        cursor.close()
        con.close()


    def update_data(self,salle):
        con = self.get_connection()
        cursor = con.cursor()
        sql = ("UPDATE salle SET description = %s, categorie = %s, capacite = %s WHERE code = %s")
        values = (salle.description,salle.categorie,salle.capacite,salle.code)

        cursor.execute(sql, values)
        con.commit()
        cursor.close()
        con.close()



