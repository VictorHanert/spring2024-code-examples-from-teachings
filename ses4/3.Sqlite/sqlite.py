import sqlite3
import os

con = sqlite3.connect(os.getcwd() + "/3.Sqlite/zoo.db")

cur = con.cursor()

cur.execute("CREATE TABLE animal(name, gender, age)")

data = [
    ("Elephant", "male", 22),
    ("Lion", "female", 10),
    ("Tiger", "male", 8)
]

cur.executemany("INSERT INTO animal VALUES(?, ?, ?)", data)
con.commit()

for row in cur.execute("SELECT * FROM animal"):
    print(row)