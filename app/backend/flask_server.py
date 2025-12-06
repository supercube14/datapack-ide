import flask
from flask import request

app = flask.Flask(__name__)

@app.route("/")
def root():
    return "A-ha!"

@app.route("/_health")
def health_check():
    return {"status": "ok"}, 200

@app.route("/_kill")
def kill_server():
    shutdown = request.environ.get("werkzeug.server.shutdown")
    if shutdown:
        shutdown()
    return {"status": "shutting down"}, 200

def start(debug=False) -> None:
    app.run(
        debug=debug,
        use_reloader=False,
        host="127.0.0.1",
        port=59776
    )