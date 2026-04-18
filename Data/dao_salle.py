import mysql.connector
import json


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
