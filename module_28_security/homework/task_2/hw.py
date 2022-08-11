from flask import Flask, Response, render_template, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def handler():
    response = make_response(render_template('index.html'))
    return response

@app.after_request
def add_cors(response: Response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers.set('Content-Security-Policy', 'default-src \'self\'')
    print(response.headers)
    return response


if __name__ == '__main__':
    app.run(port=8080, debug=True)
