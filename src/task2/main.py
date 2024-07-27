import sqlite3


class Query:

    def __init__(self, path: str) -> None:
        self.path = path

    def sql_query(self):

        query = """
            SELECT name, age
            FROM users
            WHERE age > 30
        """

        try:
            conn = sqlite3.connect(self.path)
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            return result

        except sqlite3.Error as e:
            print(e)
