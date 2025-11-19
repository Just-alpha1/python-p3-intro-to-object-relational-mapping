import sqlite3

class Model:
    table_name = None

    def __init__(self, id=None, **kwargs):
        self.id = id
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def find_all(cls, db):
        query = f"SELECT * FROM {cls.table_name}"
        cursor = db.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [cls(**dict(zip(columns, row))) for row in rows]

    def save(self, db):
        if self.id is None:
           
            columns = [attr for attr in self.__dict__ if not attr.startswith('_') and attr != 'id']
            values = [getattr(self, col) for col in columns]
            placeholders = ', '.join('?' for _ in columns)
            query = f"INSERT INTO {self.__class__.table_name} ({', '.join(columns)}) VALUES ({placeholders})"
            cursor = db.execute(query, values)
            self.id = cursor.lastrowid
        else:
       
            columns = [attr for attr in self.__dict__ if not attr.startswith('_') and attr != 'id']
            values = [getattr(self, col) for col in columns] + [self.id]
            set_clause = ', '.join(f"{col} = ?" for col in columns)
            query = f"UPDATE {self.__class__.table_name} SET {set_clause} WHERE id = ?"
            db.execute(query, values)
