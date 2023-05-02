import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE employees (
        EmpID INTEGER PRIMARY KEY,
        EmpName TEXT NOT NULL,
        EmpGender TEXT NOT NULL,
        EmpPhone TEXT NOT NULL,
        EmpBday DATE NOT NULL
    )
''')

conn.commit()
conn.close()
