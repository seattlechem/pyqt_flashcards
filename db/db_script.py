import sys
import datetime
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

    def check_book_title(self, title: str):
        sql_stm = f"SELECT book_id FROM source_book WHERE book_title='{title}'"
        row_id_list = self.get_sql_query(sql_stm)

        if len(row_id_list) == 1:
            return row_id_list[0][0]
        else:
            return None

    def save_to_source_tb(self, book_id=None, url_id=None):
        data = tuple([book_id, url_id])
        sql_stm = """INSERT INTO source (book_id, url_id) \
            VALUES (?, ?);"""
        row_id = self.post_sql_query(sql_stm, data)
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

    def post_datetime(self, created: datetime, modified: datetime):
        data = tuple([created, modified, None, None])
        sql_stm = """INSERT INTO date (created_date, modified_date, \
            last_seen_date, last_fail_date) VALUES (?, ?, ?, ?);"""
        res = self.post_sql_query(sql_stm, data)
        print(res)

if __name__ == '__main__':
    sql_conn = SqliteConnection()
    # res = sql_conn.get_last_row_column_data('subject_id', 'subject_type')
    # sql_stm = ['test book title', 1972, 'Me']
    # sql_conn.add_book_to_db(tuple(sql_stm))
    # sql_stm = 'test book title'
    # print(sql_conn.check_book_title(sql_stm))

    # print(sql_conn.save_to_source_tb(1))

    sql_conn.post_datetime(datetime.datetime.now(), datetime.datetime.now())
    # print(len(res))
    # print(str(res[0][0]))
