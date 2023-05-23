import sqlite3

def main():
    conn = None
    try:
        conn = sqlite3.connect('book_store.sqlite')
        cur = conn.cursor()

        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute(
            '''SELECT users.id, users.first_name, users.last_name, books.title
                from purchase
                join users on purchase.user_id=users.id
                join books on purchase.book_id=books.id ORDER BY users.id''')

        results = cur.fetchall()

        for row in results:
            print(f'{row[0]:5} {row[1]:15} {row[2]:15} {row[3]:10}')

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()

if __name__ == '__main__':
    main()