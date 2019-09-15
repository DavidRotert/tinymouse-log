import datetime, uuid


class LogEntry:
    NOTSET = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

    def __init__(self,
                 timestamp: int,
                 message: str,
                 extended_message: str,
                 level: int = NOTSET,
                 collection: str = "",
                 software: str = "",
                 version_major: int = 0,
                 version_minor: int = 0,
                 version_micro: int = 0,
                 line: int = 0,
                 file: str = "",
                 creation_time: int = datetime.datetime.utcnow(),
                 fields: dict = {},
                 id: str = str(uuid.uuid1())):
        """
        Model for log entry
        :param timestamp:
        :param message:
        :param extended_message:
        :param level
        :param collection:
        :param software:
        :param version_major:
        :param version_minor:
        :param version_micro:
        :param line:
        :param file:
        :param creation_time:
        :param fields:
        :param id:
        """
        self._timestamp = timestamp
        self._message = message
        self._extended_message = extended_message
        self._collection = collection
        self._software = software
        self._version_major = version_major
        self._version_minor = version_minor
        self._version_micro = version_micro
        self._line = line
        self._file = file
        self._creation_time = creation_time
        self._id = id
        self._fields = fields
        self._level = level

    def get_timestamp(self) -> int:
        return self._timestamp

    def get_message(self) -> str:
        return self._message

    def get_extended_message(self) -> str:
        return self._extended_message

    def get_collection(self) -> str:
        return self._collection

    def get_software(self) -> str:
        return self._software

    def get_version_major(self) -> int:
        return self._version_major

    def get_version_minor(self) -> int:
        return self._version_minor

    def get_version_micro(self) -> int:
        return self._version_micro

    def get_version_str(self, extension: str = "") -> str:
        return str(self.get_version_major()) + "." + str(self.get_version_minor()) + "." + \
               str(self.get_version_micro()) + extension

    def get_line(self) -> int:
        return self._line

    def get_file(self) -> str:
        return self._file

    def get_creation_time(self) -> int:
        return self._creation_time

    def get_id(self) -> str:
        return self._id

    def get_fields(self) -> dict:
        return self._fields

    def get_level(self) -> int:
        return self._level
