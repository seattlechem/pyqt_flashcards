
CREATE TABLE date
(
  date_id        INTEGER NOT NULL,
  created_date   INTEGER NOT NULL,
  modified_date  INTEGER NOT NULL,
  last_seen_date INTEGER NULL    ,
  last_fail_date INTEGER NULL    ,
  PRIMARY KEY (date_id)
);

CREATE TABLE source_book
(
  book_id    INTEGER NOT NULL,
  book_title TEXT    NOT NULL,
  year       INTEGER NOT NULL,
  author     TEXT    NOT NULL,
  PRIMARY KEY (book_id)
);

CREATE TABLE source_url
(
  url_id INTEGER NOT NULL,
  url    TEXT    NOT NULL,
  PRIMARY KEY (url_id)
);

CREATE TABLE subject_type
(
  subject_id INTEGER NOT NULL,
  subject    TEXT    NOT NULL,
  PRIMARY KEY (subject_id)
);

CREATE TABLE question_answer
(
  card_id    INTEGER NOT NULL,
  question   TEXT    NOT NULL,
  answer     TEXT    NOT NULL,
  subject_id INTEGER NOT NULL,
  date_id    INTEGER NOT NULL,
  source_id  INTEGER NULL    ,
  PRIMARY KEY (card_id),
  FOREIGN KEY (subject_id) REFERENCES subject_type (subject_id),
  FOREIGN KEY (date_id) REFERENCES date (date_id),
  FOREIGN KEY (source_id) REFERENCES source (source_id)
);

CREATE TABLE source
(
  source_id INTEGER NOT NULL,
  book_id   INTEGER NULL    ,
  url_id    INTEGER NULL    ,
  PRIMARY KEY (source_id),
  FOREIGN KEY (book_id) REFERENCES source_book (book_id),
  FOREIGN KEY (url_id) REFERENCES source_url (url_id)
);
