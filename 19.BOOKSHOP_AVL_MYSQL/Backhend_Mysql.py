import time
from random import randint
import mysql.connector




def create_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kamal@1991",
        database="bookshop",

    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(ID INTEGER AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(255) ,Year INTEGER(10) ,Author VARCHAR(255),ISBN "
                "INTEGER(10) )")
    conn.commit()
    conn.close()

def insert(Title,Year,Author,ISBN):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kamal@1991",
        database="bookshop",

    )

    cur = conn.cursor()
    query ="INSERT INTO book(Title,Year,Author,ISBN) VALUES(%s,%s,%s,%s)"
    values = (Title,Year,Author,ISBN)
    cur.execute(query,values)
    conn.commit()
    conn.close()

#insert("bowl",5,100.0)

def view():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kamal@1991",
        database="bookshop",

    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()

    return rows
    conn.close()


def delete(ID):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kamal@1991",
        database="bookshop",

    )
    cur = conn.cursor()
    query = "DELETE FROM book WHERE ID=%s"
    values =(ID,)
    cur.execute(query,values)
    conn.commit()
    print(cur.rowcount, "record(s) deleted")
    conn.close()

def update(ID,Title,Year,Author,ISBN):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kamal@1991",
        database="bookshop",

    )
    cur = conn.cursor()
    query = "UPDATE book SET Title=%s,Year=%s,Author=%s,ISBN=%s WHERE ID=%s"
    values = (Title,Year,Author,ISBN,ID)
    cur.execute(query,values)
    conn.commit()
    conn.close()

def Search(Title="",Year="",Author="",ISBN=""):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kamal@1991",
        database="bookshop",

    )
    cur = conn.cursor()
    query = "SELECT * FROM book WHERE Title=%s OR Year=%s OR Author=%s OR ISBN=%s"
    values = (Title, Year, Author, ISBN)
    cur.execute(query,values)
    rows = cur.fetchall()
    return rows
    conn.close()


create_table()
#insert("kala chaman",1992,"kamal singh",20202022)

#delete(1)
#print(Search(Year=1991))
#update(2,"kala chuha",1993,"kamal singh",20202023)
print(view())