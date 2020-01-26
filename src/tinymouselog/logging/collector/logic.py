from ... db.connectors import MongoDBConnector
import datetime


def add_log_entry(entry_dict, collector):
    connector = MongoDBConnector.MongoDBConnector(database="Test")
    log = validate_entry_fields_and_modificate_with_defaults(entry_dict)
    connector.insert(log, collection=collector)


def validate_entry_fields_and_modificate_with_defaults(entry_dict):
    """Validates fields and adds default values if required keys not exist."""
    if "_id" in entry_dict:
        raise ValueError("The key '_id' can not be used in log entry because it is dynamically generated.")

    if "timestamp" not in entry_dict:
        entry_dict["timestamp"] = datetime.datetime.utcnow()
    else:
        if type(entry_dict["timestamp"]) != int:
            raise ValueError("The key 'timestamp' has to be the time in UTC.")
        else:
            entry_dict["timestamp"] = datetime.datetime.utcfromtimestamp(entry_dict["timestamp"])

    if "level" not in entry_dict:
        entry_dict["level"] = "trace"
    else:
        if type(entry_dict["level"]) != str or entry_dict["level"] not in ("trace", "debug", "info", "warn", "error",
                                                                           "critical"):
            raise ValueError("The key 'level' has to be a string with one of the following values: 'trace', "
                             "'debug', 'info', 'warn', 'error' or 'critical'.")

    if "message" not in entry_dict:
        raise ValueError("The log requires a key 'message' with a log message string.")

    return entry_dict
