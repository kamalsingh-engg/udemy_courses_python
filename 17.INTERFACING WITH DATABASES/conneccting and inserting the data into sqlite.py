"""
we are going to connect the python with the sqlite3 here so the code i am using is the basic that is the required to
write the code
"""
"""
import sqlite3
conn = sqlite3.connect("little.db")
cur = conn.cursor()
cur.execute("CREATE TABLE store(item TEXT ,quantity INTEGER ,price REAL )")
conn.commit()
conn.close()

"""
import sqlite3
def create_table():
    conn = sqlite3.connect("little.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT ,quantity INTEGER ,price REAL )")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("little.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

#insert("bowl",5,100.0)

def view():
    conn = sqlite3.connect("little.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())

"""
connecting to sqlite and creating a DB which is "little db"

create_table function points
1. after creating it we need to go the cursor that is in the create_table function 
2. exceute means whatever you want to function " so in it to create the table we create the table in it 
3. next need to commit the connection 
4. and then close to the connection 

insert_table function points 
1. same we need to add means to connect to the DB 
2. the open through the cursor 
3. value need to insert and that can be insert through function argument which can be add as ? 
4. then close and commit

then insert the argument through the insert function 

view function points 
1. connect 
2. excecute for select from store 
3. fatch the all data 
4. close 
5. print 

"""

