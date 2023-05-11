import sqlite3

def main():
    conn = sqlite3.connect('Database.db')

    cur = conn.cursor()

    cur.execute('''INSERT INTO Table1 (first_name, last_name, age) VALUES ("Ріккі", "Мартін", 42), ("Ірина", "Білик", 52), ("Тіна", "Кароль", 38), ("Ольга", "Сумська", 52), ("Микола", "Тищенко", 42)''')

    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()