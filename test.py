import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("./my_flashcards.sqlite")

# Create the application
app = QApplication(sys.argv)

# Try to open the connection and handle possible errors
def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("./db/flashcards.db")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True

def insert_source_url():
  insertDataQuery = QSqlQuery()
  insertDataQuery.prepare(
      """
      INSERT INTO source_url (
          url_id,
          url
      )
      VALUES (?, ?)
      """
  )

  # Sample data
  data = [
      (1, "http://www.chosun.com")
  ]

  # Use .addBindValue() to insert data
  for url_id, url in data:
      insertDataQuery.addBindValue(url_id)
      insertDataQuery.addBindValue(url)
      insertDataQuery.exec()


# Create the application's window
if not createConnection():
    sys.exit(1)

insert_source_url()

win = QLabel("Connection Successfully Opened!")
win.setWindowTitle("App Name")
win.resize(200, 100)
win.show()
sys.exit(app.exec_())
