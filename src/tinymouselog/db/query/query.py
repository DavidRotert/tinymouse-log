def parse(query, translator):
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
                raise SqlSyntaxError("Syntax error in SQL statement: Use SELECT COUNT([field]) ... .")
        elif token.is_delete():
            if last_token is not None:
                raise SqlSyntaxError("Syntax error in SQL statement: Cannot use a DELETE statement behind "
                                     + last_token + ".")
            last_token = "DELETE"

        elif last_token in ("SELECT", "DELETE"):
            pass

class BaseStatement:
    pass

class AggregateFunction:
    pass

class Select:
    pass

class Token:
    def __init__(self, token: str):
        self._token = token

    def is_select(self):
        syntax = "select"
        return self.is_syntax(syntax)

    def is_delete(self):
        syntax = "delete"
        return self.is_syntax(syntax)

    def is_count(self):
        syntax = "count("
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
