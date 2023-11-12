import sqlite3

DB_NAME = 'db_ex.sqlite'

con = sqlite3.connect(DB_NAME)
cur = con.cursor()

cur.execute("""
    SELECT Product.maker, Product.model, PC.model
    FROM Product
    JOIN PC ON Product.type = 'PC' AND
               Product.model = PC.model AND
               PC.speed >= 450
""")

for i in cur:
    print(i)