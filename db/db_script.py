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

    def run_sql_query(self, sql_stm: str):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_stm)
            res = cur.fetchall()

        # self.close_db(cur)
        return res

    def add_subject_to_db(self, data: tuple):

        sql_stm = """INSERT into subject_type (subject) \
            VALUES (?);"""

        cur = self.conn.cursor()
        cur.execute(sql_stm, data)
        self.conn.commit()

    def get_last_row_column_data(self, column_name: str, table_name: str):
        # open db
        # self.open_db()

        sql_stm = f"SELECT {column_name} FROM {table_name} ORDER BY {column_name} DESC LIMIT 1"
        res = self.run_sql_query(sql_stm)

        return res

    def get_all_subjects(self):

        sql_stm = 'SELECT subject FROM subject_type'
        res = self.run_sql_query(sql_stm)
        # self.conn.close()
        return res


if __name__ == '__main__':
    sql_conn = SqliteConnection()
    res = sql_conn.get_last_row_column_data('subject_id', 'subject_type')
    print(len(res))
    print(str(res[0][0]))
