from flask import Flask, request, make_response
from tinymouselog.logging.collector import logic


app = Flask(__name__)


@app.route("/logging/logs/<collector>", methods=["POST"])
def post_log_entry(collector: str):
    if request.content_type != "application/json":
        resp = make_response("Endpoint expects 'application/json' as content type.", 415)
        resp.headers["Content-Type"] = "application/json"
        return resp

    entry_data = request.get_json()
    logic.add_log_entry(entry_data, collector)

    resp = make_response("", 204)
    resp.headers["Content-Type"] = "application/json"
    return resp


@app.route("/logging/logs/<collector>/<uuid>", methods=["GET"])
def get_log_entry(collector: str, uuid: str):
    pass


if __name__ == "__main__":
    app.run("localhost", 3636, True)
