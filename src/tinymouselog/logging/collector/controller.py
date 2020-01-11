from flask import Flask, request
from tinymouselog.logging.collector.logic import *

app = Flask(__name__)


@app.route("/logging/<application>/logs", methods=["POST"])
def post_log_entry(application: str):
    entry_data = request.get_json()
    add_log_entry(entry_data, application)
    return "test"


if __name__ == "__main__":
    app.run("localhost", 3636, True)
