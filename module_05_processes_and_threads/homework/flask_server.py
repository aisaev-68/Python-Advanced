import sys

import flask

app = flask.Flask(__name__)


@app.endpoint('/test', )
def test_endpoint():
    return 'Run Flask server, port 5001!'


if __name__ == '__main__':

    for port in sys.stdin:
        app.run(port=int(port))

