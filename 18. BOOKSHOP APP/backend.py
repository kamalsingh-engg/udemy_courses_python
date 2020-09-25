


import sqlite3
def create_table():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(ID INTEGER PRIMARY KEY, Title TEXT ,Year INTEGER ,Author TEXT,ISBN "
                "INTEGER )")
    conn.commit()
    conn.close()

def insert(Title,Year,Author,ISBN):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(Title,Year,Author,ISBN))
    conn.commit()
    conn.close()

#insert("bowl",5,100.0)

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(ID):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE ID=?",(ID,))
    conn.commit()
    conn.close()

def update(ID,Title,Year,Author,ISBN):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET Title=?,Year=?,Author=?,ISBN=? WHERE ID=?" ,(Title,Year,Author,ISBN,ID))
    conn.commit()
    conn.close()

def Search(Title="",Year="",Author="",ISBN=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE Title=? OR Year=? OR Author=? OR ISBN=? ",(Title, Year, Author, ISBN,))
    rows = cur.fetchall()
    conn.close()
    return rows

#create_table()
#insert("kala chaman",1992,"kamal singh",20202022)

#delete(1)
#print(Search(Year=1991))
update(2,"kala chuha",1993,"kamal singh",20202023)
print(view())