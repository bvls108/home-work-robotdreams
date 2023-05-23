import sqlite3

def main():
    conn = sqlite3.connect('database.sqlite')

    cur = conn.cursor()

    cur.execute('''SELECT age, COUNT (age) FROM users GROUP BY AGE ORDER BY COUNT (age) DESC, AGE ''')


    results = cur.fetchall()

    print('age  / users')

    for row in results:
        print(f'{row[0]:4} {row[1]:4}')

    conn.close()

if __name__ == '__main__':
    main()