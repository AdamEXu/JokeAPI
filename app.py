from flask import Flask, jsonify, request, render_template
import json
import random
import datetime
from lepton import generate_joke

with open('jokes.json', 'r') as f:
  jokes = json.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    random.seed()
    return jsonify(random.choice(jokes))
  else:
    random.seed()
    joke = random.choice(jokes)
    # calculate joke of the day
    random.seed(hash(datetime.datetime.now().strftime('%Y-%m-%d')))
    joke_number = random.randint(0, len(jokes) - 1)
    joke_of_the_day = jokes[joke_number]
    # render html page
    html_page = render_template('index.html', joke=joke, html_page="<html>...</html>", jokes=jokes, joke_of_the_day=joke_of_the_day)
    return render_template('index.html', joke=joke, html_page=html_page, jokes=jokes, joke_of_the_day=joke_of_the_day)

@app.route('/puns', methods=['POST'])
def puns():
  data = request.get_json(silent=True)
  if data and 'number' in data:
    number = int(data['number'])
  else:
    number = len(jokes)
  
  return jsonify(random.choices(jokes, k=number))

@app.route('/joke-of-the-day', methods=['POST'])
def joke_of_the_day():
  date = None
  if request.is_json:
    data = request.get_json(silent=True)
    if data and 'date' in data:
      date = data['date']
  
  if date is None: 
    date = datetime.datetime.now().strftime('%Y-%m-%d')
  
  random.seed(hash(date))
  joke_number = random.randint(0, len(jokes) - 1)
  joke_of_the_day = jokes[joke_number]
  return jsonify(joke_of_the_day)

@app.route('/generate-joke', methods=['POST'])
def generate_joke_api():
  data = request.get_json(silent=True)
  if data and 'prompt' in data:
    prompt = data['prompt']
  else:
    prompt = ""
  joke_string = generate_joke(prompt)
  try:
    joke_json = json.loads(joke_string)
    return jsonify(joke_json)
  except json.JSONDecodeError:
    return jsonify({"error": "Something went wrong while generating the joke"}), 500

@app.route('/search-jokes', methods=['POST'])
def search_jokes():
  data = request.get_json(silent=True)
  if data and 'query' in data:
    query = data['query']
  else:
    return jsonify({"error": "No query provided"}), 400 
  if data and 'limit' in data:
    limit = int(data['limit'])
  else:
    limit = 10

  results = []
  for joke in jokes:
    if query in joke['q'] or query in joke['a'] or query in joke['tags']:
      results.append(joke)
      if len(results) == limit:
        break
  return jsonify(results)

@app.route('/get-jokes-by-tag', methods=['POST'])
def get_jokes_by_tag():
  data = request.get_json(silent=True)
  if data and 'tag' in data:
    tag = data['tag']
  else:
    return jsonify({"error": "No tag provided"}), 400 

  results = []
  for joke in jokes:
    if tag in joke['tags']:
      results.append(joke)
  return jsonify(results)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)