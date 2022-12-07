import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
path = 'assets/leaderbard.json'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_word', methods=['GET'])
def get_word():
    length = request.args.to_dict()['length']
    params = {'length': length,
              'words': 1}
    response = requests.get('https://random-word-api.vercel.app/api', params=params)
    return json.dumps(response.text)


@app.route('/get_rules')
def get_rules():
    data = []
    with open('assets/rules.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)

@app.route('/lb', methods=['GET', 'POST']) # leaderboard
def lb():
    resList = []
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump([], f)
    if request.method == 'POST':
        dati  = request.json
        if dati is not None and len(dati)>0:
            with open(path, 'r') as f:
                resList = json.load(f)
                resList.append(dati)
            with open(path, 'w') as f:
                json.dump(resList, f, indent=1)
    with open(path, 'r') as f:
        resList = json.load(f)
    return json.dumps(sorted(resList, key=lambda v: v['points'], reverse=True))

if __name__ == '__main__':
    app.debug = True
    app.run()
