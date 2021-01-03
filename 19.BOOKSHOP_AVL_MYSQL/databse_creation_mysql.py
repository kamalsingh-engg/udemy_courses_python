import time
from random import randint
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="kamal@1991",

)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS bookshop")