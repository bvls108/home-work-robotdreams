import sqlite3

def main():
    conn = sqlite3.connect('database.sqlite')

    cur = conn.cursor()

    cur.execute('''SELECT COUNT (*) FROM users WHERE age >30''')

    results = cur.fetchone()

    print(results)

    conn.close()

if __name__ == '__main__':
    main()