import sqlite3
conn = sqlite3.connect('StudentInfo',timeout=2.0)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Student')
cur.execute('CREATE TABLE Student (name TEXT,rno INTEGER)')
cur.execute('INSERT INTO Student VALUES(?,?)',('Mahesh',45))
cur.execute('INSERT INTO Student VALUES(?,?)',('Rahul',30))


cur.execute('select * from Student')
print("data in databse using fetchall(): ")
print(cur.fetchall())
conn.close()