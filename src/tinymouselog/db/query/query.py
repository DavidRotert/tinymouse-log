def translate_from_sql(query, translator):
    tokens = query.split(" ")

    query_obj: BaseStatement = None
    last_token = None
    fields = []
    statement_end = False
    for t in tokens:
        token = Token(t)
        if token.is_empty():
            continue
        elif token.is_select():
            if last_token is not None:
                raise SqlSyntaxError("Syntax error in SQL statement: Cannot use a SELECT statement behind "
                                     + last_token + ".")
            last_token = "SELECT"
        elif token.is_count():
            if last_token is not None:
                raise SqlSyntaxError("Syntax error in SQL statement: Use SELECT COUNT() ... .")
        elif token.is_delete():
            if last_token is not None:
                raise SqlSyntaxError("Syntax error in SQL statement: Cannot use a DELETE statement behind "
                                     + last_token + ".")
            last_token = "DELETE"

        elif last_token in ("SELECT", "DELETE"):
            pass


class BaseStatement:
    def translate(self, translator):
        pass


class AggregateFunction:
    pass


class Select(BaseStatement):
    def __init__(self, table: str, fields: list = [], where=None, sort=None):
        self._table = table
        self._fields = fields
        self._where = where
        self._sort = sort

    def get_table(self):
        return self._table

    def get_fields(self):
        return self._fields

    def get_where_condition(self):
        return self._where

    def get_sort(self):
        return self._sort


class Token:
    def __init__(self, token: str):
        self._token = token

    def is_select(self):
        syntax = "select"
        return self.is_syntax(syntax)

    def is_delete(self):
        syntax = "delete"
        return False

    def is_count(self):
        syntax = "count()"
        return self.is_syntax(syntax)

    def is_syntax(self, syntax):
        return self._token.startswith(syntax) or self._token.startswith(syntax.capitalize())

    def is_empty(self):
        return self._token == ""


class SqlSyntaxError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
