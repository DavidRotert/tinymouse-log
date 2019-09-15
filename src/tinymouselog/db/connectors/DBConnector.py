class DBConnector:
    def __init__(self, database: str = None, collection: str = None, **kwargs):
        self._database = database
        self._collection = collection
        self._args = kwargs

    def insert(self, value: dict):
        pass

    def insert_values(self, values: list):
        pass

    def select(self, query: dict = {}, fields: dict = None):
        pass

    def delete(self, query: dict = {}):
        pass

    def update(self, update: dict, query: dict = {}):
        pass

    def raw_query(self, sql: str):
        pass
