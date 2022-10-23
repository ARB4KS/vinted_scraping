import sqlite3
import re

file_path = "database/db.sqlite3"
con = sqlite3.connect(file_path)
cur = con.cursor()
def add_notified_user(brand,price,type_of_clothes):
    str_brand = re.sub('[{}]', '', str(brand))
    str_clothes = re.sub('[{}]', '', str(type_of_clothes))
    a = str(price)
    str_price = re.sub('[{}]', '', a)
    new_str = str_price.replace("'", "")
    new_str.replace('"', "")
    search_query = f"SELECT * FROM roles WHERE type_of_clothes ='{str_clothes}' AND brand = '{str_brand}' AND price = {new_str}"
    cur.execute(search_query)
    fetchall = cur.fetchall()
    fetchall_len = len(fetchall)
    print(fetchall)
    if fetchall_len > 0:
        return fetchall[0][0]
    return False
def create_role(id,brand,price,type_of_clothes):
    str_brand = re.sub('[{}]', '', str(brand))
    str_clothes = re.sub('[{}]', '', str(type_of_clothes))
    a = str(price)
    str_price=re.sub('[{}]', '', a)
    new_str = str_price.replace("'", "")
    new_str.replace('"', "")

    insert_query = f"INSERT INTO roles VALUES({id},{str_brand},{float(new_str)},{str_clothes})"
    print(insert_query)
    cur.execute(insert_query)
    con.commit()
def search_users(brand,price):
    str_brand = re.sub('[{}]', '', str(brand))
    print(str_brand,price)
    print(str_brand)
    a = str(price)
    str_price = re.sub('[{}]', '', a)
    new_str = str_price.replace("'", "")
    new_str.replace('"', "")
    #search_query = cur.execute(f"SELECT * FROM roles WHERE type_of_clothes = (?)",["pulls"])
    search_query = cur.execute(f"SELECT * FROM roles WHERE type_of_clothes = 'pulls' AND  brand ='{str_brand}' AND price > {new_str}")
    fetchall = cur.fetchall()
    fetchall_len = len(fetchall)
    print(fetchall)
    if fetchall_len > 0:
        return fetchall[0][0]
    return False

    #query = cur.execute("SELECT * FROM notification_users WHERE brand = ?", [f"{str_brand}"])






