from flask import Flask

application = Flask(__name__)


@application.route("/logging/<collector>/logs", methods=["POST"])
def post_log_entry():
    pass


if __name__ == "__main__":
    application.run("localhost", 3636, True)