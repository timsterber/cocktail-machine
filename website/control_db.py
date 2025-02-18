import sqlite3
import os

class Control_DB:
    def __init__(self):
        self.DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "cocktails.db")
        self.conn = sqlite3.connect(self.DB_PATH)
        self.cursor = self.conn.cursor()
        
        self.table = "Cocktails"
        print("Class Control_DB initiated")
    
    def close(self) -> bool:
        self.conn.close()
        return True
    
    def get_cocktails_names(self) -> list:
        """Fetch all cocktail names from the database."""
        self.cursor.execute(f"SELECT name FROM {self.table}")  # Fetch only the names
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]  # Extract names into a list
    
    #! Has to be edited, when more inputs are available
    def get_cocktails(self) -> list:
        """Fetch all cocktails from the database."""
        self.cursor.execute(f"SELECT name,In1,In2,In3,In4 FROM {self.table}")
        rows = self.cursor.fetchall()
        return rows
    
    def cocktail_values_by_name(self, name) -> list:
        """Fetch a cocktail by its name."""
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE name='{name}'")
        row = self.cursor.fetchone()
        return row[2:]      # Return only the values
    
    def clear_table(self) -> bool:
        """Clear the table from all entries."""
        self.cursor.execute(f"DELETE FROM {self.table}")
        self.conn.commit()
        return True
    
    #! Has to be edited, when more inputs are available
    def add_cocktail(self, values) -> bool:
        """Add a cocktail to the database."""
        if any([value == '' for value in values]):
            return False
        self.cursor.execute(f"INSERT INTO {self.table} (name, In1, In2, In3, In4) VALUES ('{values[0]}', {values[1]}, {values[2]}, {values[3]}, {values[4]})")
        self.conn.commit()
        return True