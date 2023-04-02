import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS countries
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL)''')

cursor.execute("INSERT INTO countries (title) VALUES ('Россия')")
cursor.execute("INSERT INTO countries (title) VALUES ('США')")
cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")

cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   area REAL DEFAULT 0,
                   country_id INTEGER NOT NULL,
                   FOREIGN KEY(country_id) REFERENCES countries(id))''')

cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Ташкент', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Нью-Йорк', 2)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Ош', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Пекин', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Токио', 4)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Дублин', 5)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Владивосток', 6)")

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   city_id INTEGER NOT NULL,
                   FOREIGN KEY(city_id) REFERENCES cities(id))''')

cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Иван', 'Иванов', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Петр', 'Петров', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Анна', 'Иванова', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ирина', 'Петрова', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Константин', 'Котов', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Сергей', 'Сергеев', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ольга', 'Ильинская', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Алексей', 'Алексеев', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Елена', 'Иванова', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Артур', 'Артуров', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Мария', 'Игорева', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Дмитрий', 'Дмитриев', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Наталья', 'Партина', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Александр', 'Александров', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Екатерина', 'Васильева', 5)")

conn.commit()

cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()

print("Список городов:")
for city in cities:
    print(str(city[0]) + " - " + city[1])

city_id = int(input("Введите id города для вывода списка сотрудников или 0 для выхода: "))

while city_id != 0:

    cursor.execute('''SELECT employees.first_name, employees.last_name, countries.title, cities.title
                          FROM employees
                          JOIN cities ON employees.city_id = cities.id
                          JOIN countries ON cities.country_id = countries.id
                          WHERE cities.id = ?''', (city_id,))
    employees = cursor.fetchall()

    print("Сотрудники в городе:")
    for employee in employees:
        print(employee[0] + " " + employee[1] + " - " + employee[2] + ", " + employee[3])

    city_id = int(input("Введите id города для вывода списка сотрудников или 0 для выхода: "))

conn.close()
