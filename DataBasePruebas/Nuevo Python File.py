import sqlite3
cosas = [
('2006-01-05', 'BUY', 'RHAT', 100, 35.14),
('2006-03-28', 'BUY', 'IBM', 1000, 45.0),
('2006-04-06', 'SELL', 'IBM', 500, 53.0),
('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)
]
con = sqlite3.connect("hidalgo.db")
cur = con.cursor()
"""
cur.execute('''
    CREATE TABLE stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    price FLOAT NOT NULL
    )
    ''')
"""
cur.executemany('INSERT INTO stocks VALUES (Null,?,?,?,?,?)', cosas)
con.commit()

for row in cur.execute('SELECT * FROM stocks ORDER BY id'):
        print(row)

