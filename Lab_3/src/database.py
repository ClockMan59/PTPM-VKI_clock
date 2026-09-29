import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(":memory:")

        self.connection.execute("""
            CREATE TABLE triangles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                side1 REAL,
                side2 REAL,
                side3 REAL,
                triangle_type TEXT,
                error_message TEXT
            )
        """)

        self.connection.commit()

    def add(self, side1, side2, side3, triangle_type, error_message):
        self.connection.execute("""
            INSERT INTO triangles
            (side1, side2, side3, triangle_type, error_message)
            VALUES (?, ?, ?, ?, ?)
        """, (
            side1,
            side2,
            side3,
            triangle_type,
            error_message
        ))

        self.connection.commit()

    def get(self, side1, side2, side3):
        cursor = self.connection.execute("""
            SELECT triangle_type, error_message
            FROM triangles
            WHERE side1 = ? AND side2 = ? AND side3 = ?
        """, (side1, side2, side3))

        return cursor.fetchone()

    def delete(self, side1, side2, side3):
        self.connection.execute("""
            DELETE FROM triangles
            WHERE side1 = ? AND side2 = ? AND side3 = ?
        """, (side1, side2, side3))

        self.connection.commit()

    def close(self):
        self.connection.close()