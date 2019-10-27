from . import DBConnector
from pymongo import MongoClient


class MongoDBConnector(DBConnector):
    def __int__(self, host: str = "localhost", port: int = 27017, database: str = None, collection: str = None, **kwargs):
        super(MongoDBConnector, self).__int__(database=None, collection=None, **kwargs)
        self._host = host
        self._port = port
        self._connection = MongoClient(host=host, port=port, **kwargs)

    def _get_connection(self, database: str = None, collection: str = None):
        db_str = database
        col_str = collection
        if database is None:
            if self._databse is None:
                raise ValueError("Database string can not be none.")
            db_str = self._database

        if collection is None:
            if self._collection is None:
                raise ValueError("Collection string can not be none.")
            col_str = self._collection

        return self._connection[db_str][col_str]

    def insert(self, value: dict, database: str = None, collection: str = None):
        self._get_connection(database, collection).insert_one(value)

    def insert_values(self, values: dict, database: str = None, collection: str = None):
        self._get_connection(database, collection).insert_many(values)

    def select(self, query: dict = {}, fields: list = None, database: str = None, collection: str = None):

        self._get_connection(database, collection).find(query)