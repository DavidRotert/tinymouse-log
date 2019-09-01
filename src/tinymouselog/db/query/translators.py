from . import query


class Translator:
    def __init__(self, connection):
        self._connection = connection

    def tanslate_select(self, table: str, fields: list = [], where=None, sort=None):
        pass


class MongoDBTranslator(Translator):
    def __init__(self, connection):
        super().__init__(connection)

    def tanslate_select(self, table: str, fields: list = [], where=None, sort=None):
        collection = self._connection[table]
        aggregate = False
        return_fields = []
        for field in fields:
            if issubclass(query.AggregateFunction):
                pass
