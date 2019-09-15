from . import DBConnector
from pymongo import MongoClient


class MongoDBConnector(DBConnector):
    def __int__(self, host: str = "localhost", port: int = 27017, database: str = None, collection: str = None, **kwargs):
        super(MongoDBConnector, self).__int__(database=None, collection=None, **kwargs)
        self._host = host
        self._port = port
        self._connection = MongoClient(host=host, port=port, **kwargs)
