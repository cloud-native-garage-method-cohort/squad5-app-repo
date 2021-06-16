from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return 'Squad 5 Application'


@app.route('/getMember', methods=["GET"])
def getMember():
    r = requests.post('http://recorder:80/search',
                      data=json.loads(json.dumps(request.form, ensure_ascii=False)))
    return r.text


if __name__ == '__main__':
    app.run(port=80, Debug=False)
