import os
import sys
from flask import Flask, request, jsonify , Response, render_template

app = Flask(__name__)

@app.route('/msg')
def index():
    return "Test"

if __name__ == '__main__':
    app.run(debug=True)

sys.path.insert(0, os.path.dirname(__file__))


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python v' + sys.version.split()[0] + '\n'
    response = '\n'.join([message, version])
    return [response.encode()]
