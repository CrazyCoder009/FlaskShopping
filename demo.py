import sqlite3
con = sqlite3.connect('database.db')
c = con.cursor()
print(c.fetchall())
print(con.execute('SELECT FROM users'))
con.close()
