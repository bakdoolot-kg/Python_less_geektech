import os
import sqlite3


db_filename = 'journaldev.db'
conn = sqlite3.connect(db_filename)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
 userid INTEGER PRIMARY KEY,
 fname TEXT,
 lname TEXT,
 gender TEXT);
""")

conn.commit()


cur.execute("""
INSERT INTO users (userid, fname, lname, gender)
    VALUES ('0001', 'Alex', 'Smith', 'male');
""")

# schema_filename = 'book_schema.sql'
# db_exists = not os.path.exists(db_filename)
#
# with sqlite3.connect(db_filename) as conn:
#     cursor = conn.cursor()
#
#     cursor.execute("""
#     SELECT id, name, day_effort, book FROM chapter
#     WHERE book = 'JournalDev'
#     """)
#
#     for row in cursor.fetchall():
#         id, name, day_effort, book = row
#         print('{:2d} ({}) {:2d} ({})'.format(
#             id, name, day_effort, book))
#
#     if db_exists:
#         print('Creating schema')
#         with open(schema_filename, 'rt') as file:
#             schema = file.read()
#         conn.executescript(schema)
#
#         print('Inserting initial data')
#
#         conn.executescript("""
#         INSERT INTO book (name, topic, published)
#         VALUES ('JournalDev', 'Java', '2022-06-06');
#
#         INSERT INTO chapter (name, day_effort, book)
#         VALUES ('Java XML', 2, 'JournalDev');
#
#         INSERT INTO chapter (name, day_effort, book)
#         VALUES ('Java Generic', 1, 'JournalDev');
#
#         INSERT INTO chapter (name, day_effort, book)
#         VALUES ('Java Reflection', 3, 'JournalDev');
#         """)
#
#         conn.executescript("""
#         insert into book (name, topic, published)
#         values ('JournalDev', 'Java', '2011-01-01');
#         insert into chapter (name, day_effort, book)
#         values ('Java XML', 2,'JournalDev');
#         insert into chapter (name, day_effort, book)
#         values ('Java Generics', 1, 'JournalDev');
#         insert into chapter (name, day_effort, book)
#         values ('Java Reflection', 3, 'JournalDev');""")
#
#     else:
#         print('DB already exists.')
