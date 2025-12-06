import flask
from flask import request
import os

template_dir = os.path.abspath('app/frontend/src/templates')
static_dir = os.path.abspath('app/frontend/src/static')
app = flask.Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def root():
    print(template_dir)
    return flask.render_template('index.html')

@app.route('/_health')
def health_check():
    return {'status': 'ok'}, 200

@app.route('/_kill')
def kill_server():
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if shutdown:
        shutdown()
    return {'status': 'shutting down'}, 200

def start(debug=False) -> None:
    app.run(
        debug=debug,
        use_reloader=False,
        host='127.0.0.1',
        port=59776
    )