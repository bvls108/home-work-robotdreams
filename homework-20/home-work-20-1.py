import sqlite3

def main():
    conn = sqlite3.connect('Database.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Table1 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, age INTEGER)''')

    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()