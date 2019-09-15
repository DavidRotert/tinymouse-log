from flask import Flask

application = Flask(__name__)


@application.route("/logging/<collector>/logs", methods=["POST"])
def post_log_entry():
    pass

