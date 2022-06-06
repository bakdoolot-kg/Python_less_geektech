import sqlite3


class ORM:

    def create_table(self, table_name):
        con = sqlite3.connect('last_lesson')
        cursor = con.cursor()

        cursor.execute(
            f"""CREATE TABLE {table_name} (id INTEGER, name VARCHAR(10))"""
        )

        cursor.close()

orm = ORM()
# orm.create_table('bakdoolot')