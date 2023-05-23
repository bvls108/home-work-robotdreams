import sqlite3

def main():
    conn = None
    try:
        conn = sqlite3.connect('book_store.sqlite')
        cur = conn.cursor()

        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute(
            '''SELECT purchase.id, purchase.date, users.first_name, users.last_name
                FROM purchase join users on purchase.user_id = users.id''')

        results = cur.fetchall()

        for row in results:
            print(f'{row[0]:5} {row[1]:25} {row[2]:10} {row[3]:10}')

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()

if __name__ == '__main__':
    main()