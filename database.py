import sqlite3
file_path = "database/db.sqlite3"
con = sqlite3.connect(file_path)
cur = con.cursor()
def add_notified_user(id,brand,price):
    query = "CREATE TABLE IF NOT EXISTS notification_users(id,brand,price)"
    cur.execute(query)


