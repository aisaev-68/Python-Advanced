from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def handler():
    print(request)
    return jsonify({"Hello": "User"})


@app.route('/names/<name>', methods=['POST'])
def add_name(name):
    print(request.method)
    return jsonify({"Hello": name})


@app.after_request
def add_cors(response: Response):
    response.headers.add('Access-Control-Allow-Origin', 'https://www.google.com')
    response.headers.add('Access-Control-Allow-Headers', 'X-My-Fancy-Header')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response


if __name__ == '__main__':
    app.run(port=8080, debug=True)
