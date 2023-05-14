import sqlite3

def main():
    conn = sqlite3.connect('books_database.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users (users_id INTEGER PRIMARY KEY NOT NULL, first_name TEXT, last_name TEXT, age INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS publishing_house (publishing_house_id INTEGER PRIMARY KEY NOT NULL, name TEXT, rating INTEGER DEFAULT 5)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS books (books_id INTEGER PRIMARY KEY NOT NULL, title TEXT, author TEXT, year INTEGER, price REAL, publishing_house_id INTEGER, FOREIGN KEY (publishing_house_id) REFERENCES publishing_house(publishing_house_id))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS purchases (purchases_id INTEGER PRIMARY KEY NOT NULL, users_id INTEGER, books_id INTEGER,  date TEXT, FOREIGN KEY (users_id) REFERENCES users(users_id), FOREIGN KEY (books_id) REFERENCES books(books_id))''')


    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()