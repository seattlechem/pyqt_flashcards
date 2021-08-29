## Features
1. Able to add subject
2. Subject are auto populated from db
3. Search for book via title and author
4. if title and author can be found in the source_book table
5. Do not insert it, instead return the book_id, just update note
6. push button (book search)
7. add "Select ....." into combobox option as a default before connecting to \
db
7. disable start button unless two combobox indexes are not zero (completed: 2021/01/25)
8. Show clickable url (not yet)
9. Test only cards added today
    now = datetime.datetime.now()
    search for matching year/mm/dd
    select * from date where strftime('%Y/%m/%d', created_date)='2021/08/28';
    select * from question_answer where date_id in (select date_id from date where strftime('%Y/%m/%d', created_date)='2021/08/28');
    select * from question_answer where date_id in (select date_id from date where strftime('%Y/%m/%d', created_date)=strftime('%Y/%m/%d', datetime('now'));
    select * from question_answer where date_id in (select date_id from date where strftime('%Y-%m-%d', created_date) = date('now', '-1 day'));
    ELECT * FROM question_answer WHERE date_id IN (SELECT date_id \
                    FROM date WHERE strftime('%Y-%m-%d', created_date)\
                    BETWEEN date('now', '-5 day') AND date('now'))

## How to use
1. workon pyqt
2. ./main.py

## SQLite
1. ctrl shift p
2. sqlite: open database
3. navigate to db file

## How to add additional test scripts
1. test_tab.py
2. sql_stm_dic

## TODO
1. subject selection no needed for "test all cards added today"
2. display "last seen"
3. test all cards tested today that failed more than two times
4. link is still remained after test is completed
