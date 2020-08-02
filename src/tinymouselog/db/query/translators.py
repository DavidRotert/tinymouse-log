from . import query


class Translator:
    def __init__(self, connection):
        self._connection = connection

    def tanslate_select(self, statement):
        pass


class MongoDBTranslator(Translator):
    def __init__(self, connection):
        super().__init__(connection)

    def tanslate_select(self, statement: query.Select):
        collection = self._connection[statement.get_table()]
        aggregate = False
        return_fields = []
        for field in statement.get_fields():
            if isinstance(field, query.AggregateFunction):
                aggregate = True
