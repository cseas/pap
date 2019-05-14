import os
import sqlite3

db_filename = 'EmpDb'
schema_filename = 'EmpDb.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')
        
        conn.execute("""
        insert into Employee (EmpID, DeptName, GrossSalary)
        values (1, 'CSE', 300)
        """)

        conn.execute("""
        insert into Employee (EmpID, DeptName, GrossSalary)
        values (2, 'Quality Control', 200)
        """)

        conn.execute("""
        insert into Employee (EmpID, DeptName, GrossSalary)
        values (3, 'Quality Control', 100)
        """)
    else:
        print('Database exists, assume schema does, too.')
