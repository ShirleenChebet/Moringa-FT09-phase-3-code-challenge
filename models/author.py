from database.connection import Connection
class Author:
    def __init__(self, id: int = None, name: str = ""):
        if id is not None and not isinstance(id, int):
            raise ValueError("ID must be an integer.")
        self.id = id
        self.name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer or None.")
        self._id = value


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name is not None:
            raise AttributeError("Cannot change name after initialization.")
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    def articles(self):
        query = "SELECT * FROM articles WHERE author_id = ?;"
        return Connection.get_db_connection().execute(query, (self.id,)).fetchall()

    def magazines(self):
        query = """
            SELECT DISTINCT m.* 
            FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?;
        """
        return Connection.get_db_connection().execute(query, (self.id,)).fetchall()
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        return Connection.get_db_connection().execute(query).fetchall()

