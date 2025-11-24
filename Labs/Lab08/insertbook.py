import sqlite3
con = sqlite3.connect('pfda.lb') #Name 0f the DB
cur = con.cursor()

result = cur.execute("select*from book")
print (result.fetchone())

#Insert book
sql = """ 
INSERT INTO book VALUES 
    ('Harry Potter', 'Just Kidding', '112344'),
    ('Harry Potter does something profound','JK Rowling','123444')
"""

cur.execute(sql)
con.commit()

result = cur.execute("select*from book")
print (result.fetchone())

con.close()