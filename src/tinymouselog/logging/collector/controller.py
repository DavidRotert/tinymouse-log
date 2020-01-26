from flask import Flask, request
from tinymouselog.logging.collector import logic


app = Flask(__name__)


@app.route("/logging/logs/<collector>", methods=["POST"])
def post_log_entry(collector: str):
    if request.content_type != "application/json":
        return "Endpoint expects 'application/json' as content type.", 415

    entry_data = request.get_json()
    logic.add_log_entry(entry_data, collector)

    return "test", 200


if __name__ == "__main__":
    app.run("localhost", 3636, True)
