import sqlite3

def main():
    conn = sqlite3.connect('database.sqlite')

    cur = conn.cursor()

    cur.execute('''SELECT * FROM users WHERE age >30''')

    results = cur.fetchall()

    for row in results:
        print(f'{row[0]:5} {row[1]:25}')

    conn.close()

if __name__ == '__main__':
    main()