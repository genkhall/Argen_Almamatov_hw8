import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_products(conn, product: tuple):
    try:
        sql = '''INSERT INTO products 
             ( product_title, price, quantity) 
             VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, product: tuple):
    try:
        sql = '''update products set quantity = ? where id = ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)


def update_price(conn, product: tuple):
    try:
        sql = '''update products set price = ? where id = ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)


def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)


def select_all_products(conn):
    try:
        sql = '''select * from products
                '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


def select_by_price_and_quantity(conn, limit):
    try:
        sql = '''select * from products where price < ? and quantity > ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


def search_by_word(conn, word):
    try:
        sql = '''select * from products where product_title like ?
                '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


data_base_name = 'hw.db'

sql_create_products_table = '''
CREATE TABLE products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0 
)
'''

connection_to_db = create_connection(data_base_name)
create_table(connection_to_db, sql_create_products_table)


create_products(connection_to_db, ('Пепси', 80.5, 10))
create_products(connection_to_db, ('Сэндвич', 75.89, 5))
create_products(connection_to_db, ('Мыло детское', 30.25, 8))
create_products(connection_to_db, ('Вода газированная', 30.15, 4))
create_products(connection_to_db, ('ASU', 35.67, 12))
create_products(connection_to_db, ('Вода со вкусом банана', 49.99, 9))
create_products(connection_to_db, ('Шоколад', 120.34, 15))
create_products(connection_to_db, ('Печенье шоколадное', 115.58, 7))
create_products(connection_to_db, ('Печенье овсяные', 138.12, 15))
create_products(connection_to_db, ('Чипсы', 125.19, 11))
create_products(connection_to_db, ('Чипсы со вкусом краба', 123.79, 8))
create_products(connection_to_db, ('Halls', 34.45, 17))
create_products(connection_to_db, ('Жвачка', 35.23, 10))
create_products(connection_to_db, ('Ручка синяя', 96.5, 6))
create_products(connection_to_db, ('Молоко', 97.1, 12))
update_quantity(connection_to_db, (13, 7))
update_price(connection_to_db, (33.33, 12))
delete_product(connection_to_db, 2)
select_all_products(connection_to_db)
select_by_price_and_quantity(connection_to_db, (100, 5))
search_by_word(connection_to_db, 'Мыло')

connection_to_db.close()


if connection_to_db is not None:
    print("Succesfully conneccted")
