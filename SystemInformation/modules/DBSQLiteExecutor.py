import sqlite3
def connect():
    global conn
    conn = sqlite3.connect('database.db')
def executeSQL(exec):
    cur = conn.cursor()
    cur.execute(exec)
    conn.commit()
def exandinarraySQL(exec):
    cur = conn.cursor()
    cur.execute(exec)
    array=cur.fetchall()
    conn.commit()
    return array
def lenTable(db_name):
    count=0
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {db_name}")
    for i in cur.fetchall():
        count+=1
    conn.commit()
    return count
def loadSQLite():
    executeSQL("""CREATE TABLE IF NOT EXISTS db_students(
   student_id INT PRIMARY KEY,
   full_name TEXT,
   class_id TEXT);
   """)
    executeSQL("""CREATE TABLE IF NOT EXISTS db_items(
   id PRIMARY KEY,
   item_name TEXT,
   date LONG,
   score INT,
   student_id INT);
   """)