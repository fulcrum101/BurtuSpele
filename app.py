from flask import Flask, redirect, url_for, render_template, request
import requests, json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/get_word', methods=['GET'])
# def get_word():
#     length = request.args.to_dict().get('length', type=int)
#     query = {'minLength': length,
#              'maxLength' : length,
#              'api_key': }
#     response = requests.get('https://api.wordnik.com/v4/words.json/',
#                             params=query).json()
#     return json.dumps(response)

@app.route('/get_rules')
def get_rules():
    data = []
    with open('assets/rules.json', 'r') as f:
        data = json.load(f)
    return json.dumps(data)



app.run(debug=True)
