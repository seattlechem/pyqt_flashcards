import sys
import datetime
import sqlite3


class SqliteConnection():
    def __init__(self):
        super().__init__()
        self.conn = self.open_db('./db/flashcards_datetime.db')

    def open_db(self, db_file_path: str):
        return sqlite3.connect(db_file_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

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

    def post_sql_query(self, sql_stm: str):
        cur = self.conn.cursor()
        cur.execute(sql_stm)
        self.conn.commit()
        return cur.lastrowid

    def add_subject_to_db(self, subject: str):

        sql_stm = f"INSERT into subject_type (subject) \
            VALUES ('{subject}');"

        self.post_sql_query(sql_stm)

    def add_book_to_db(self, book_title: str, year: int, author: str, \
        book_note=None):

        sql_stm = f"INSERT INTO source_book (book_title, year, author, \
            book_note) VALUES ('{book_title}', '{year}', '{author}', \
                '{book_note}');"

        row_id = self.post_sql_query(sql_stm)

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
        sql_stm = f"INSERT INTO source (book_id, url_id) \
            VALUES ('{book_id}', '{url_id}');"
        row_id = self.post_sql_query(sql_stm)
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

    def post_datetime(self, created: datetime, modified: datetime,
                      last_seen=None, last_fail=None):
        sql_stm = f"INSERT INTO date (created_date, modified_date, \
            last_seen_date, last_fail_date) VALUES ('{created}', '{modified}', \
                '{last_seen}', '{last_fail}');"
        res = self.post_sql_query(sql_stm)
        return res

    def get_datetime(self, date_id: int):
        sql_stm = f"SELECT created_date from date where date_id='{date_id}'"
        res = self.get_sql_query(sql_stm)
        return res

    def post_question_answer_tb(self, question: str, answer: str,
                                subject_id: int, date_id: int, source_id: int):
        sql_stm = f"INSERT INTO question_answer (question, answer, subject_id,\
            date_id, source_id) VALUES ('{question}', '{answer}', \
                '{subject_id}', '{date_id}', '{source_id}')"
        res = self.post_sql_query(sql_stm)


if __name__ == '__main__':
    sql_conn = SqliteConnection()
    # res = sql_conn.get_last_row_column_data('subject_id', 'subject_type')
    # sql_stm = ['test book title', 1972, 'Me']
    sql_conn.add_book_to_db('test book tilte', 1972, 'me')
    # sql_stm = 'test book title'
    # print(sql_conn.check_book_title(sql_stm))

    # print(sql_conn.save_to_source_tb(1))

    # sql_conn.post_datetime(datetime.datetime.now(), datetime.datetime.now())
    # res = sql_conn.get_datetime(1)
    # print(type(res[0][0]))
    # print(res[0][0])

    # print(len(res))
    # print(str(res[0][0]))
