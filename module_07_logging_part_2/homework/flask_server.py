from flask import Flask


app = Flask(__name__)


@app.route("/<message>")
def test(message):
    return f'Была получена фраза {message}'


if __name__ == '__main__':
    app.run(debug=True)