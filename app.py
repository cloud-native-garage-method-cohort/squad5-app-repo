from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return 'Squad 5 Application'


@app.route('/getMember', methods=["GET"])
def getMember():
    r = requests.get('http://recorder:80/')
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
