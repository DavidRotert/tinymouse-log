class DBConnector:
    def __init__(self, database: str = None, collection: str = None, **kwargs):
        self._database = database
        self._collection = collection
        self._args = kwargs

    def insert(self, value: dict, database: str = None, collection: str = None):
        pass

    def insert_values(self, values: list, database: str = None, collection: str = None):
        pass

    def select(self, query, fields: list = None, database: str = None, collection: str = None):
        pass

    def delete(self, query, database: str = None, collection: str = None):
        pass

    def update(self, update: dict, query, database: str = None, collection: str = None):
        pass

    def raw_query(self, sql: str):
        pass
