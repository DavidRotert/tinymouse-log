from flask import Flask, request
from . import logic

app = Flask(__name__)


@app.route("/logging/logs/<collector>", methods=["POST"])
def post_log_entry(collector: str):
    entry_data = request.get_json()
    logic.add_log_entry(entry_data, collector)
    return "test"


if __name__ == "__main__":
    app.run("localhost", 3636, True)
