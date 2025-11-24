import sqlite3
con = sqlite3.connect('pfda.lb') #Name 0f the DB
cur = con.cursor()

cur.execute("CREATE TABLE book(title, author, ISBN)")

con.close()