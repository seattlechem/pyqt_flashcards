import sys
import sqlite3


class SqliteConnection():
    def __init__(self):
        super().__init__()
        self.conn = self.open_db('./db/flashcards.db')

    def open_db(self, db_file_path: str):
        return sqlite3.connect(db_file_path)

    def close_db(self, cur):
        if self.conn:
            cur.close()
            self.conn.close()
        else:
            print("Unable to close db; db is not open")
            sys.exit(1)

    def get_sql_query(self, sql_stm: str):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_stm)
            res = cur.fetchall()

        # self.close_db(cur)
        return res

    def post_sql_query(self, sql_stm: str, data: tuple):
        cur = self.conn.cursor()
        cur.execute(sql_stm, data)
        self.conn.commit()
        return cur.lastrowid

    def add_subject_to_db(self, data: tuple):

        sql_stm = """INSERT into subject_type (subject) \
            VALUES (?);"""

        self.post_sql_query(sql_stm, data)

    def add_book_to_db(self, data: tuple):

        sql_stm = """INSERT INTO source_book (book_title, year, author) \
            VALUES (?, ?, ?);"""

        row_id = self.post_sql_query(sql_stm, data)

        # return id
        return row_id

    def get_last_row_column_data(self, column_name: str, table_name: str):
        # open db
        # self.open_db()

        sql_stm = f"SELECT {column_name} FROM {table_name} ORDER BY \
            {column_name} DESC LIMIT 1"

        res = self.get_sql_query(sql_stm)

        return res

    def get_all_subjects(self):

        sql_stm = 'SELECT subject FROM subject_type'
        res = self.get_sql_query(sql_stm)
        # self.conn.close()
        return res


if __name__ == '__main__':
    sql_conn = SqliteConnection()
    # res = sql_conn.get_last_row_column_data('subject_id', 'subject_type')
    sql_stm = ['test book title', 1972, 'Me']
    sql_conn.add_book_to_db(tuple(sql_stm))
    # print(len(res))
    # print(str(res[0][0]))
