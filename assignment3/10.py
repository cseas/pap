import sqlite3

db_filename = 'EmpDb'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select SUM(GrossSalary) from Employee where DeptName = 'Quality Control'
    """)

    for row in cursor.fetchall():
        print(row)
