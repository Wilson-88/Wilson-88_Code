# func_py_sqlite_create_table.py
import sqlite3

def func_py_sqlite_create_table(db_name="data.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    conn.close()

func_py_sqlite_create_table()
