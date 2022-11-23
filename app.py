import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_word', methods=['GET'])
def get_word():
    length = request.args.to_dict()['length']
    params = {'length': length}
    response = requests.get('https://random-word-api.herokuapp.com/word', params=params)
    return json.dumps(response.text)


@app.route('/get_rules')
def get_rules():
    data = []
    with open('assets/rules.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)


if __name__ == '__main__':
    app.debug = True
    app.run()
