
import sqlite3 as sqlite
import time

import pandas as pd


class Crud:
    """Simple CRUD class for SQLite databases."""

    def __init__(
        self,
        database,
        table,
        column_1="",
        column_2="",
        column_3=""
    ):
        self.connection = sqlite.connect(database)
        self.cursor = self.connection.cursor()

        self.table = table
        self.column_1 = column_1
        self.column_2 = column_2
        self.column_3 = column_3

    def create_table(self):
        """Create table if it does not exist."""
        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id INTEGER PRIMARY KEY,
                {self.column_1} TEXT,
                {self.column_2} TEXT,
                {self.column_3} DATE
            )
        """
        self.execute(query)

    def validate_date(self, date_value):
        """Validate date format DD-MM-YYYY."""
        try:
            day, month, year = map(int, date_value.split("-"))
            current_year = int(time.strftime("%Y"))

            if (
                1920 <= year <= current_year
                and 1 <= month <= 12
                and 1 <= day <= 31
            ):
                return True

            return False

        except ValueError:
            return False

    def insert_data(self, record_id, value_1, value_2, value_3):
        """Insert data into the table."""
        if not self.validate_date(value_3):
            print("Invalid date. Data not inserted.")
            return

        query = f"""
            INSERT INTO {self.table}
            VALUES (?, ?, ?, ?)
        """

        try:
            self.cursor.execute(
                query,
                (record_id, value_1, value_2, value_3)
            )
            self.save_changes()

        except Exception as error:
            print(f"Error: {error}")

    def read_all(self):
        """Read all records."""
        query = f"SELECT * FROM {self.table}"
        self.show_data(query)

    def read_ordered(self, field):
        """Read records ordered by a field."""
        query = f"SELECT * FROM {self.table} ORDER BY {field}"
        self.show_data(query)

    def search(self, column, value):
        """Search records by column."""
        query = f"SELECT * FROM {self.table} WHERE {column} = ?"
        self.show_data(query, (value,))

    def update(self, column, new_value, condition_column, condition_value):
        """Update records."""
        query = (
            f"UPDATE {self.table} "
            f"SET {column} = ? "
            f"WHERE {condition_column} = ?"
        )

        self.execute(query, (new_value, condition_value))

    def delete(self, column, value):
        """Delete records."""
        query = f"DELETE FROM {self.table} WHERE {column} = ?"
        self.execute(query, (value,))

    def execute(self, query, params=None):
        """Execute SQL query."""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            self.save_changes()

        except Exception as error:
            print(f"Error: {error}")

    def show_data(self, query, params=None):
        """Display query results as DataFrame."""
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        data = self.cursor.fetchall()

        df = pd.DataFrame(
            data,
            columns=["ID", "Nombre", "Apellido", "Fecha_Nacimiento"]
        )

        print(df)

    def save_changes(self):
        """Commit changes."""
        self.connection.commit()

    def close_database(self):
        """Close database connection."""
        self.connection.close()
