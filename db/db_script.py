import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class SqliteConnection(QSqlDatabase):
    def __init__(self):
        super().__init__()
        self.conn = self.addDatabase("QSQLITE")

    def set_db(self, db_name: str):
        self.conn.setDatabaseName(db_name)

    def open_db(self):
        self.set_db('./db/flashcards.db')
        if not self.conn.open():
            print('Unable to open db')
            sys.exit(1)

    def close_db(self):
        if self.conn.isOpen():
            self.conn.close()
        else:
            print("Unable to close db; db is not open")
            sys.exit(1)

    def add_subject_to_db(self, data):
        self.open_db()
        query = QSqlQuery()

        query.prepare(
            """
            INSERT INTO subject_type (
                subject_id,
                subject
            )
            VALUES (?, ?)
            """
        )

        for subject_id, subject in data:
            query.addBindValue(subject_id)
            query.addBindValue(subject)
            query.exec()

        self.close_db()

    def get_all_subjects(self):
        res = []
        self.open_db()
        sql_statement = 'SELECT subject FROM subject_type'
        query = QSqlQuery(sql_statement)

        while query.next():
            res.append(query.value(0))

        return res
